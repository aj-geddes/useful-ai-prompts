---
category: creation
compatible_models:
- GPT-4
- Claude 3
- Gemini Pro
- GPT-3.5
date: '2025-07-20'
description: A practical code generation assistant that helps you create well-structured, maintainable code following best practices. Provide your requirements and I'll generate production-ready code with proper architecture, error handling, and documentation.
layout: prompt
prompt: "import { TaskRepository } from '../repositories/TaskRepository';\nimport { Task, CreateTaskRequest, TaskStatus } from '../models/Task';\nimport { NotificationService } from './NotificationService';\n\nexport class TaskService {\n  constructor(\n    private taskRepository: TaskRepository,\n    private notificationService: NotificationService\n  ) {}\n\n  async createTask(taskData: CreateTaskRequest, userId: string): Promise<Task> {\n    // Validation\n    this.validateTaskData(taskData);\n\n    // Create task\n    const task = await this.taskRepository.create(taskData, userId);\n\n    // Send notification if task is assigned\n    if (task.assigneeId && task.assigneeId !== userId) {\n      await this.notificationService.sendTaskAssignedNotification(\n        task.assigneeId,\n        task\n      );\n    }\n\n    return task;\n  }\n\n  async getTaskById(taskId: string, userId: string): Promise<Task> {\n    const task = await this.taskRepository.findById(taskId);\n    \n    if (!task) {\n      throw new Error('Task not found');\n    }\n\n    // Check if user has access to this task\n    await this.validateTaskAccess(task, userId);\n\n    return task;\n  }\n\n  async getProjectTasks(\n    projectId: string, \n    userId: string,\n    filters?: {\n      status?: TaskStatus;\n      assigneeId?: string;\n      page?: number;\n      limit?: number;\n    }\n  ): Promise<{ tasks: Task[]; total: number }> {\n    // Validate user access to project\n    await this.validateProjectAccess(projectId, userId);\n\n    const limit = filters?.limit || 50;\n    const offset = filters?.page ? (filters.page - 1) * limit : 0;\n\n    const tasks = await this.taskRepository.findByProject(projectId, {\n      ...filters,\n      limit,\n      offset\n    });\n\n    // Get total count for pagination\n    const total = await this.getTaskCount(projectId, filters);\n\n    return { tasks, total };\n  }\n\n  async updateTask(\n    taskId: string, \n    updates: Partial<Task>, \n    userId: string\n  ): Promise<Task> {\n    const existingTask = await this.taskRepository.findById(taskId);\n    \n    if (!existingTask) {\n      throw new Error('Task not found');\n    }\n\n    await this.validateTaskAccess(existingTask, userId);\n\n    // Validate updates\n    this.validateTaskUpdates(updates);\n\n    const updatedTask = await this.taskRepository.update(taskId, updates);\n\n    // Send notifications for status changes\n    if (updates.status && updates.status !== existingTask.status) {\n      await this.handleStatusChangeNotifications(updatedTask, existingTask);\n    }\n\n    return updatedTask;\n  }\n\n  async deleteTask(taskId: string, userId: string): Promise<void> {\n    const task = await this.taskRepository.findById(taskId);\n    \n    if (!task) {\n      throw new Error('Task not found');\n    }\n\n    await this.validateTaskAccess(task, userId);\n    await this.taskRepository.delete(taskId);\n  }\n\n  private validateTaskData(taskData: CreateTaskRequest): void {\n    if (!taskData.title?.trim()) {\n      throw new Error('Task title is required');\n    }\n\n    if (taskData.title.length > 200) {\n      throw new Error('Task title must be less than 200 characters');\n    }\n\n    if (taskData.description && taskData.description.length > 2000) {\n      throw new Error('Task description must be less than 2000 characters');\n    }\n\n    if (taskData.dueDate && taskData.dueDate < new Date()) {\n      throw new Error('Due date cannot be in the past');\n    }\n  }\n\n  private validateTaskUpdates(updates: Partial<Task>): void {\n    if (updates.title !== undefined) {\n      if (!updates.title?.trim()) {\n        throw new Error('Task title cannot be empty');\n      }\n      if (updates.title.length > 200) {\n        throw new Error('Task title must be less than 200 characters');\n      }\n    }\n\n    if (updates.description !== undefined && updates.description && updates.description.length > 2000) {\n      throw new Error('Task description must be less than 2000 characters');\n    }\n  }\n\n  private async validateTaskAccess(task: Task, userId: string): Promise<void> {\n    // Implementation would check if user has access to the project\n    // This could involve checking project membership, role permissions, etc.\n  }\n\n  private async validateProjectAccess(projectId: string, userId: string): Promise<void> {\n    // Implementation would validate user access to project\n  }\n\n  private async getTaskCount(projectId: string, filters?: any): Promise<number> {\n    // Implementation would return total count for pagination\n    return 0;\n  }\n\n  private async handleStatusChangeNotifications(updatedTask: Task, originalTask: Task): Promise<void> {\n    // Send appropriate notifications based on status change\n    if (updatedTask.status === TaskStatus.DONE) {\n      await this.notificationService.sendTaskCompletedNotification(updatedTask);\n    }\n  }\n}"
related_prompts:
- api-design-expert
- database-design-expert
- software-architecture-expert
slug: code-generation-expert
tags:
- code generation
- software development
- programming
- application development
- clean code
title: Code Generation Expert
use_cases:
- application development
- API creation
- algorithm implementation
- code refactoring
version: 2.0.0
---
