"use client";

import { useRef, useEffect, useState } from "react";
import mermaid from "mermaid";
import { IconButton } from "@mui/material";
import RefreshIcon from "@mui/icons-material/Refresh";
import ZoomInIcon from "@mui/icons-material/ZoomIn";
import ZoomOutIcon from "@mui/icons-material/ZoomOut";
import FullscreenIcon from "@mui/icons-material/Fullscreen";
import DownloadIcon from "@mui/icons-material/Download";
import ResetIcon from "@mui/icons-material/Autorenew";
import Tooltip from "@mui/material/Tooltip";
import { NoDataOverlay } from "../noDataOverlay";
import { useGetAllEventmessages } from "@/api/eventmessages/eventmessages";
import { mutate } from "swr";
import { LoadingOverlay } from "../join/loadingOverlay";
import { generateMermaidString } from "./helpers";

const SequenceDiagram = () => {
  const {
    data: eventMessagesData,
    isLoading: loadingEventMessages,
    swrKey: eventMessagesKeyFunc,
  } = useGetAllEventmessages();

  const mermaidRef: any = useRef(null);
  const [scale, setScale] = useState(1);
  const hasData = eventMessagesData?.data && eventMessagesData?.data.length > 0;
  // const hasData = true;

  const mermaidString = generateMermaidString(eventMessagesData?.data);

  useEffect(() => {
    if (!loadingEventMessages && hasData)
      mermaid.initialize({
        startOnLoad: false,
        securityLevel: "loose",
        sequence: {
          mirrorActors: false,
        },
      });

    if (mermaidRef.current) {
      mermaidRef.current.innerHTML = mermaidString;
      mermaid.init(undefined, mermaidRef.current);
    }
  }, [loadingEventMessages, hasData, mermaidString]);

  useEffect(() => {
    if (mermaidRef.current) {
      const svg = mermaidRef.current.querySelector("svg");
      if (svg) {
        svg.style.transform = `scale(${scale})`;
        svg.style.transformOrigin = "top left"; // Set transform origin to top left
        mermaidRef.current.style.width = `${
          svg.getBoundingClientRect().width * scale
        }px`;
        mermaidRef.current.style.height = `${
          svg.getBoundingClientRect().height * scale
        }px`;
      }
    }
  }, [scale]);

  const onRefresh = () => {
    const eventMessagesKey =
      typeof eventMessagesKeyFunc === "function"
        ? eventMessagesKeyFunc()
        : eventMessagesKeyFunc;

    if (eventMessagesKey) {
      mutate(eventMessagesKey);
    }
  };

  const zoomIn = () => {
    setScale((scale) => scale * 1.1);
  };

  const zoomOut = () => {
    setScale((scale) => scale / 1.1);
  };

  const resetZoom = () => {
    setScale(1);
  };

  const viewInFullScreen = () => {
    if (mermaidRef.current) {
      const svg = mermaidRef.current.querySelector("svg");
      const serializer = new XMLSerializer();
      const svgBlob = new Blob([serializer.serializeToString(svg)], {
        type: "image/svg+xml",
      });
      const url = URL.createObjectURL(svgBlob);
      window.open(url, "_blank");
    }
  };

  const downloadAsPng = () => {
    if (mermaidRef.current) {
      const svg = mermaidRef.current.querySelector("svg");
      const svgData = new XMLSerializer().serializeToString(svg);

      // Create a canvas element to convert SVG to PNG
      const canvas = document.createElement("canvas");
      const svgSize = svg.getBoundingClientRect();
      canvas.width = svgSize.width;
      canvas.height = svgSize.height;
      const ctx = canvas.getContext("2d");
      const img = document.createElement("img");

      img.onload = () => {
        ctx?.drawImage(img, 0, 0);
        const pngData = canvas.toDataURL("image/png");

        // Trigger download
        const link = document.createElement("a");
        link.download = "sequence-diagram.png";
        link.href = pngData;
        link.click();
      };

      img.src =
        "data:image/svg+xml;base64," +
        btoa(unescape(encodeURIComponent(svgData)));
    }
  };

  if (loadingEventMessages)
    return <LoadingOverlay title="Loading Diagram" subtitle="Please wait..." />;

  return (
    <div className="flex w-full flex-col items-end">
      {hasData ? (
        <>
          <div className="flex w-full justify-end gap-2.5 mb-5">
            <Tooltip placement="top" title="Refresh Diagram">
              <IconButton color="default" onClick={onRefresh}>
                <RefreshIcon />
              </IconButton>
            </Tooltip>
            <Tooltip title="Zoom In" placement="top">
              <IconButton color="primary" onClick={zoomIn}>
                <ZoomInIcon />
              </IconButton>
            </Tooltip>
            <Tooltip title="Zoom Out" placement="top">
              <IconButton color="primary" onClick={zoomOut}>
                <ZoomOutIcon />
              </IconButton>
            </Tooltip>
            <Tooltip title="Reset" placement="top">
              <IconButton color="primary" onClick={resetZoom}>
                <ResetIcon />
              </IconButton>
            </Tooltip>
            <Tooltip title="View in Fullscreen" placement="top">
              <IconButton color="primary" onClick={viewInFullScreen}>
                <FullscreenIcon />
              </IconButton>
            </Tooltip>
            <Tooltip title="Download as PNG" placement="top">
              <IconButton color="primary" onClick={downloadAsPng}>
                <DownloadIcon />
              </IconButton>
            </Tooltip>
          </div>
          <div className="w-full h-full overflow-auto p-2.5 box-border">
            <div className="mermaid" ref={mermaidRef}></div>
          </div>
        </>
      ) : (
        <div className="flex w-full justify-center items-center">
          <NoDataOverlay label="No Activity yet" />
        </div>
      )}
    </div>
  );
};

export default SequenceDiagram;
