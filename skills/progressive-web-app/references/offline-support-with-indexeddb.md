# Offline Support with IndexedDB

## Offline Support with IndexedDB

```typescript
// db/notesDB.ts
import { openDB, DBSchema, IDBPDatabase } from "idb";

interface Note {
  id: string;
  title: string;
  content: string;
  timestamp: number;
  synced: boolean;
}

interface NotesDB extends DBSchema {
  notes: {
    key: string;
    value: Note;
    indexes: { "by-timestamp": number; "by-synced": boolean };
  };
}

let db: IDBPDatabase<NotesDB>;

export async function initDB() {
  db = await openDB<NotesDB>("notes-db", 1, {
    upgrade(db) {
      const store = db.createObjectStore("notes", { keyPath: "id" });
      store.createIndex("by-timestamp", "timestamp");
      store.createIndex("by-synced", "synced");
    },
  });
  return db;
}

export async function addNote(note: Omit<Note, "timestamp">) {
  return db.add("notes", {
    ...note,
    timestamp: Date.now(),
    synced: false,
  });
}

export async function getNotes(): Promise<Note[]> {
  return db.getAll("notes");
}

export async function getUnsyncedNotes(): Promise<Note[]> {
  return db.getAllFromIndex("notes", "by-synced", false);
}

export async function updateNote(id: string, updates: Partial<Note>) {
  const note = await db.get("notes", id);
  if (note) {
    await db.put("notes", { ...note, ...updates });
  }
}

export async function markAsSynced(id: string) {
  await updateNote(id, { synced: true });
}
```
