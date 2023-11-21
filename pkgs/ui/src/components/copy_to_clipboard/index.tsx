import { useState } from "react";
import { Button, Snackbar } from "@mui/material";

const CopyToClipboard = ({ contentRef }: { contentRef: any }) => {
  const [open, setOpen] = useState(false);
  const handleClick = () => {
    if (contentRef.current) {
      const text = contentRef.current.textContent;
      navigator.clipboard.writeText(text);
      setOpen(true);
    }
  };

  return (
    <>
      <Button onClick={handleClick}>Copy</Button>
      <Snackbar
        open={open}
        onClose={() => setOpen(false)}
        autoHideDuration={2000}
        message="Copied to clipboard"
      />
    </>
  );
};
export default CopyToClipboard;
