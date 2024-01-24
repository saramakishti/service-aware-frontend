# CopyToClipboard Component

## Overview

The `CopyToClipboard` component is a versatile UI component designed to facilitate copying text to the user's clipboard. It can copy text from two sources: directly from a passed text string prop (`textToCopy`) or from the text content of a referenced div element (`contentRef`). The component includes a clickable icon and displays a confirmation snackbar notification once the copy action is successful.

## Props

The component accepts the following props:

1. `textToCopy` (optional): A string representing the direct text you want to copy. If provided, this text is copied to the clipboard when the icon is clicked.

2. `contentRef` (optional): A `RefObject<HTMLDivElement>` that references a div element. The text content of this div is copied to the clipboard if `textToCopy` is not provided.

## Behavior

- Copy Action: When the copy icon is clicked, the component:

  - Prioritizes copying the text from the textToCopy prop if it's provided and not an empty string.
  - If textToCopy is not provided or is empty, it then attempts to copy the text content of the element referenced by contentRef.
  - Uses the Clipboard API (`navigator.clipboard.writeText`) to copy the text to the user's clipboard.
  - Displays a snackbar notification confirming the copy action if successful.

- Snackbar Notification: A temporary notification that:
  - Appears after the text is successfully copied.
  - Displays the message "Copied to clipboard!".
  - Disappears automatically after 2000 milliseconds and is positioned at the bottom left of the screen.

## How to Use

1. Import the `CopyToClipboard` component.
2. Use the component in one of the following ways:
3. Pass a `textToCopy` prop with the text you want to copy, OR
4. Pass a `contentRef` prop pointing to a div element containing the text you want to copy.
5. Render the `CopyToClipboard` component where you want the copy icon to appear.

## Example

Using `textToCopy` prop:

```javascript
import CopyToClipboard from "./CopyToClipboard";

const SomeComponent = () => {
  return (
    <div>
      <CopyToClipboard textToCopy="Text to be copied" />
    </div>
  );
};

export default SomeComponent;
```

Using `contentRef` prop:

```javascript
import React, { useRef } from "react";
import CopyToClipboard from "./CopyToClipboard";

const SomeComponent = () => {
  const textRef = useRef(null);

  return (
    <div>
      <div ref={textRef}>Text to copy from ref</div>
      <CopyToClipboard contentRef={textRef} />
    </div>
  );
};

export default SomeComponent;
```
