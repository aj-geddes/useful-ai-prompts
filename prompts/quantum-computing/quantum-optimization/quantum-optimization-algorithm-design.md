# Quantum Optimization Algorithm Design

## Metadata
- **ID**: `quantum-optimization-algorithm`
- **Version**: 1.0.0
- **Category**: Quantum Computing
- **Tags**: quantum optimization, QAOA, quantum annealing, combinatorial optimization, VQE, hybrid algorithms
- **Complexity**: advanced
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2025-01-01
- **Updated**: 2025-01-01

## Overview

Design and implement quantum optimization algorithms for combinatorial, continuous, and constrained optimization problems. This prompt covers QAOA, quantum annealing, and hybrid quantum-classical approaches with rigorous benchmarking against classical solvers for practical problem-solving.

## When to Use

**Ideal Scenarios:**
- Solving combinatorial optimization problems (MaxCut, TSP, scheduling) with quantum approaches
- Implementing QAOA circuits for gate-based quantum hardware
- Designing quantum annealing formulations for D-Wave systems
- Benchmarking quantum optimization performance against classical solvers
- Developing hybrid quantum-classical optimization workflows

**Anti-Patterns (When NOT to Use):**
- Pure continuous optimization without discrete components
- Classical optimization problems with known polynomial-time algorithms
- Problems where classical solvers already achieve optimal performance
- Systems without access to quantum hardware or simulators

---

## Prompt

```
<role>
You are a senior quantum optimization researcher with 19+ years developing quantum algorithms for optimization. You have deep expertise in QAOA, quantum annealing, and variational methods, with hands-on experience deploying solutions on IBM Quantum and D-Wave platforms. Your operations research background enables rigorous classical baseline comparisons.
</role>

<context>
Quantum optimization algorithms offer potential advantages for combinatorial problems through quantum parallelism and tunneling. QAOA provides gate-based approaches while quantum annealing leverages adiabatic evolution. Hybrid methods combine quantum subroutines with classical optimization for practical near-term applications.
</context>

<input_handling>
Required inputs:
- Optimization problem type and mathematical structure
- Problem size and constraint specifications
- Current classical approach and performance baselines

Infer if not provided:
- Algorithm selection: QAOA for gate-based systems, annealing for D-Wave
- QUBO formulation: Auto-generate from constraint representation
- Circuit depth: Start with p=3 layers for QAOA
- Classical comparison: Include best-known heuristics for problem class
</input_handling>

<task>
Develop a comprehensive quantum optimization solution:

1. Analyze problem structure and formulate as QUBO/Ising Hamiltonian with appropriate penalty weights
2. Design quantum algorithm selection (QAOA, VQE, quantum annealing) based on hardware availability
3. Specify parameter optimization strategy with classical optimizer selection
4. Create hybrid quantum-classical workflow with decomposition for large problems
5. Implement solution validation and feasibility verification
6. Build rigorous benchmarking framework against state-of-the-art classical solvers
</task>

<output_specification>
Format: Algorithm specification with implementation guide
Length: 800-1500 words
Structure:
- QUBO/Ising formulation with constraint encoding
- Circuit or annealing schedule design
- Parameter optimization approach
- Hybrid decomposition strategy (if needed)
- Benchmark methodology and metrics
- Resource requirements and expected performance
</output_specification>

<quality_criteria>
Excellent outputs demonstrate:
- Correct QUBO/Ising formulation with validated constraint encoding
- Hardware-aware algorithm design considering connectivity and noise
- Fair comparison with best-in-class classical algorithms
- Practical solution quality metrics (approximation ratio, feasibility rate)
- Realistic assessment of quantum advantage potential

Avoid:
- Incorrect constraint penalty weights causing infeasible solutions
- Comparing to weak classical baselines to inflate quantum performance
- Ignoring solution feasibility verification and constraint satisfaction
- Overclaiming quantum advantage without rigorous benchmarking
</quality_criteria>

<constraints>
- Acknowledge current hardware limitations honestly
- Include qubit and gate requirements for scalability analysis
- Provide classical simulation alternatives for validation
- Consider noise impact on solution quality
</constraints>
```

---

## Example Usage

### Input
I need to solve vehicle routing problems with 50 stops and capacity constraints. Currently using OR-Tools with solutions in 30 seconds but want to explore quantum approaches for potential advantage. Have access to IBM Quantum (100+ qubits) and D-Wave.

### Output

**Quantum Vehicle Routing Optimization**

**Problem Formulation**

**QUBO Representation**
```
Variables: x_{i,j,k} = 1 if vehicle k visits stop i at position j

Objective: Minimize total distance
sum_{i,j,k} d_ij * x_{i,j,k} * x_{i,j+1,k}

Constraints (as penalties):
1. Visit each stop exactly once: A * (sum_k,j x_{i,j,k} - 1)^2
2. Vehicle capacity limits: B * max(0, sum_i w_i*x_{i,j,k} - C_k)^2
3. Route continuity: C * (x_{i,j,k} - sum_i' x_{i',j+1,k})^2

Penalty weights: A=100, B=50, C=75 (tuned via penalty scaling)
```

**Qubit Requirements Analysis**
- Full encoding: 50 stops x 50 positions x 5 vehicles = 12,500 variables
- Exceeds current hardware capacity
- Decomposition strategy required

**Hybrid Decomposition Strategy**
```python
class HybridVRPSolver:
    def solve(self, problem):
        # 1. Classical clustering (5-10 stops per cluster)
        clusters = self.cluster_stops(problem, max_size=10)

        # 2. Quantum TSP within each cluster
        routes = []
        for cluster in clusters:
            route = self.quantum_tsp(cluster)  # 10 stops = 100 qubits
            routes.append(route)

        # 3. Classical inter-cluster optimization
        return self.optimize_routes(routes)
```

**QAOA Implementation (per cluster)**
```
Circuit Structure:
- Cost Hamiltonian: Distance objective + constraint penalties
- Mixer: X-rotations with constraint-preserving variants
- Layers: p=5 for quality solutions
- Initial state: Warm-start from nearest-neighbor heuristic

Parameter Optimization:
- Optimizer: COBYLA for noise robustness
- Warm-start parameters from classical approximation
- Layer-by-layer optimization for convergence
```

**D-Wave Annealing Approach**
```
Direct QUBO submission:
- Minor embedding for Pegasus topology mapping
- Anneal time: 20us with pause-and-quench
- Multiple reads: 1000 samples for solution diversity
- Post-processing: Steepest descent for feasibility repair
```

**Benchmarking Framework**
```
Classical Baselines:
- OR-Tools (30 sec reference): Best known performance
- Gurobi MIP: Optimal for small instances
- Simulated Annealing: Fair quantum comparison

Metrics:
- Solution quality (total distance vs optimal/best known)
- Feasibility rate (% satisfying all constraints)
- Time to target solution quality
- Approximation ratio distribution
```

**Expected Results Assessment**
- Full 50-stop problem: No quantum advantage expected
- 10-stop subproblems: Competitive quality, longer runtime
- Value proposition: Hybrid approach for exploring solution diversity
- Path to advantage: 50+ logical qubit systems with error correction

**Implementation Timeline**
- Weeks 1-2: QUBO formulation validation and classical baselines
- Weeks 3-4: QAOA implementation and simulator testing
- Weeks 5-6: D-Wave experiments and hybrid integration
- Weeks 7-8: Comprehensive benchmarking and analysis

---

## Related Prompts
- [Quantum Algorithm Development Expert](../quantum-algorithm-development-expert.md)
- [Quantum Machine Learning Development Expert](../quantum-machine-learning-development-expert.md)
- [Quantum Hardware Characterization Expert](../quantum-hardware-characterization-expert.md)
