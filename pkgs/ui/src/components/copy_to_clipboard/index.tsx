import { useState, RefObject } from "react";
import { Tooltip, Snackbar } from "@mui/material";
import ContentCopyIcon from "@mui/icons-material/ContentCopy";

const CopyToClipboard = ({
  contentRef,
  textToCopy,
}: {
  contentRef?: RefObject<HTMLDivElement>;
  textToCopy?: string;
}) => {
  const [open, setOpen] = useState(false);

  const handleClick = () => {
    // Prioritize direct text copy if 'textToCopy' is provided
    const text = textToCopy || contentRef?.current?.textContent || "";
    const copiedText = textToCopy ? JSON.stringify(text, null, 2) : text;

    if (text) {
      navigator.clipboard.writeText(copiedText).then(
        () => {
          setOpen(true);
        },
        (err) => {
          console.error("Could not copy text: ", err);
        },
      );
    }
  };

  return (
    <>
      <Tooltip placement="left" title="Copy to Clipboard">
        <ContentCopyIcon onClick={handleClick} className="cursor-pointer" />
      </Tooltip>
      <Snackbar
        open={open}
        onClose={() => setOpen(false)}
        autoHideDuration={2000}
        message="Copied to clipboard!"
        anchorOrigin={{
          vertical: "bottom",
          horizontal: "left",
        }}
      />
    </>
  );
};

export default CopyToClipboard;
