# SummaryDetails Component

## Overview

The `SummaryDetails` component is a flexible UI component designed to display a summary of details related to a specific entity in a card format. It is equipped with optional functionalities such as refreshing the data.

## Props

The component accepts the following props:

1. `entity`: An object representing the entity whose details are to be displayed. It should have a name and details, where details is an array of `EntityDetails` objects.

2. `hasRefreshButton` (optional): A boolean indicating if a Refresh button should be displayed. If true, the button is shown, allowing the user to refresh the entity details.

3. `fake` (optional): A boolean indicating if the displayed data is fake. If true, a label '(Fake Data)' is displayed in the card's header.

4. `onRefresh` (optional): A function to be called when the Refresh button is clicked. It should handle the logic for refreshing the entity details.

## UI Structure

- The component starts with a flex container displaying the entity's name and optional button (Refresh) based on the props.
- If the entity has details (checked by `hasDetails`), it displays a card containing:
  - A `CardHeader` with a subheader indicating it's a summary and whether the data is fake.
  - A `CopyToClipboard` component attached to the card's action, allowing the user to copy the details.
  - A `CardContent` section listing all the details. Each detail is displayed as a `Typography` component, showing the label and value of each `EntityDetails` item.

## How to Use

1. Import the `SummaryDetails` component.
2. Create an entity object with a name and details, where details is an array of objects with label and value.
3. Optionally, decide if you want the Refresh functionality by setting `hasRefreshButton` to `true`.
4. If using the `Refresh` functionality, provide an `onRefresh` function to handle the logic.
5. Render the `SummaryDetails` component with the desired props.

## Example

```javascript
<SummaryDetails
  entity={{
    name: "Sample Entity",
    details: [
      { label: "Detail 1", value: "Value 1" },
      { label: "Detail 2", value: "Value 2" },
      // ... more details
    ],
  }}
  hasRefreshButton={true}
  onRefresh={() => {
    // handle refresh button logic/callback
  }}
/>
```
