# Task 2: Importing Existing Data

## Task 2: Importing Existing Data

**Goal:** Import data from an external source

**Supported formats:** CSV, JSON, XML, Excel

**Steps:**

1. Click **Import** in the toolbar
2. Choose your data source:
   - **From File:** Upload a file from your computer
   - **From URL:** Enter a URL to fetch data
   - **From Database:** Connect to an external database

3. **For File Import:**

   ```
   - Click "Choose File"
   - Select your CSV/JSON file
   - Click "Upload"
   ```

4. **Map your fields**
   - Match source columns to destination fields
   - Set data types for each field
   - Preview the mapping

   | Source Field | Destination Field | Type |
   | ------------ | ----------------- | ---- |
   | email        | Email Address     | Text |
   | name         | Full Name         | Text |
   | created      | Created Date      | Date |

5. **Import settings**
   - Duplicate handling: Skip, Update, or Create new
   - Error handling: Stop on error or Continue
   - Batch size: 100 records per batch

6. Click **Start Import**

**Progress:** You'll see a progress bar showing:

- Records processed
- Successful imports
- Errors encountered
