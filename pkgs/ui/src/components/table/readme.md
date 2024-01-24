# CustomTable Component

## Overview

The `CustomTable` component is a dynamic and flexible table designed to display data in a structured tabular format. It is highly customizable, allowing specific rendering for different data types and providing a user-friendly display for loading and empty data states.

## Props

The component accepts the following props:

1. `configuration`: An array of `CustomTableConfiguration` objects defining the structure and customization options for table columns, including:

- `key`: Corresponds to the key in the data objects for the column.
- `label`: Text label for the column header.
- `render` (optional): A function for custom rendering of the cell's content.
- `data`: An array of data objects, each representing a row in the table.
- `loading` (optional): If `true`, displays a loading state (skeleton screen).
- `tkey`: A unique key for the table, used for constructing unique cell keys.

## Behavior

- **Loading State**: Displays a `Skeleton` loader when `loading` is `true`.
- **Empty Data State**: Displays a `NoDataOverlay` component with a message if no data is available.
- **Data Rendering**:
  - Dynamically renders cells based on `configuration`.
  - Handles different data types:
    - Joins array elements with a comma.
    - Shows a disabled checkbox for boolean values.
    - Uses the provided `render` function for custom rendering.
  - Logs a warning if a cell's value is an object (not an array), and no `render` function is provided.
- **Error Handling**: Each cell is wrapped in an `ErrorBoundary` component for graceful error handling.

## How to Use

1. Import the `CustomTable` component.
2. Define the `configuration` for table columns.
3. Provide `data` as an array of objects corresponding to the configuration.
4. Optionally, control the loading state with the `loading` prop.
5. Provide a unique `tkey` for the table.

## Example

```javascript
import CustomTable from "./CustomTable";

const tableConfig = [
  { key: "name", label: "Name" },
  { key: "age", label: "Age" },
  {
    key: "isActive",
    label: "Active",
    render: (isActive) => (isActive ? "Yes" : "No"),
  },
];

const tableData = [
  { name: "John Doe", age: 30, isActive: true },
  { name: "Jane Smith", age: 25, isActive: false },
];

const SomeComponent = () => {
  return (
    <div>
      <CustomTable
        configuration={tableConfig}
        data={tableData}
        loading={false}
        tkey="unique-table-key"
      />
    </div>
  );
};

export default SomeComponent;
```
