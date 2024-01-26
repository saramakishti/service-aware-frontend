"use client";

import { useRef, useEffect, useState } from "react";
import mermaid from "mermaid";
import {
  Button,
  Card,
  Chip,
  Dialog,
  DialogActions,
  Tooltip,
  DialogContent,
  DialogContentText,
  DialogTitle,
  IconButton,
  List,
  TextField,
} from "@mui/material";
//Icons
import RefreshIcon from "@mui/icons-material/Refresh";
import ZoomInIcon from "@mui/icons-material/ZoomIn";
import ZoomOutIcon from "@mui/icons-material/ZoomOut";
import FullscreenIcon from "@mui/icons-material/Fullscreen";
import DownloadIcon from "@mui/icons-material/Download";
import ResetIcon from "@mui/icons-material/Autorenew";
import FilterAltIcon from "@mui/icons-material/FilterAlt";

// Custom Components
import { NoDataOverlay } from "../noDataOverlay";
import { LoadingOverlay } from "../join/loadingOverlay";

import { useGetAllEventmessages } from "@/api/eventmessages/eventmessages";
import { mutate } from "swr";

import { extractAllEventMessages, generateMermaidString } from "./helpers";
import CopyToClipboard from "../copy_to_clipboard";
import { formatDateTime, getGroupById } from "@/utils/helpers";

const SequenceDiagram = () => {
  const {
    data: eventMessagesData,
    isLoading: loadingEventMessages,
    swrKey: eventMessagesKeyFunc,
  } = useGetAllEventmessages();

  const [scale, setScale] = useState(1);
  const [openFilters, setOpenFilters] = useState(false);
  const [sequenceNr, setSequenceNr] = useState("");

  const mermaidRef: any = useRef(null);

  const hasData = eventMessagesData?.data && eventMessagesData?.data.length > 0;
  const mermaidString = generateMermaidString(eventMessagesData?.data);
  const allEventMessages = extractAllEventMessages(eventMessagesData?.data);
  const dataDependency = JSON.stringify(hasData ? eventMessagesData?.data : "");

  useEffect(() => {
    const currentMermaidRef = mermaidRef?.current;

    if (!loadingEventMessages && hasData) {
      if (
        currentMermaidRef &&
        !currentMermaidRef.getAttribute("data-processed")
      ) {
        mermaid.initialize({
          startOnLoad: false,
          securityLevel: "loose",
          sequence: {
            mirrorActors: true,
            showSequenceNumbers: true,
          },
        });
      }

      if (currentMermaidRef) {
        currentMermaidRef.innerHTML = mermaidString;
        mermaid.init(undefined, currentMermaidRef);
      }
    }
    return () => {
      if (currentMermaidRef) {
        currentMermaidRef.removeAttribute("data-processed");
        currentMermaidRef.innerHTML = "";
      }
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [dataDependency]);

  useEffect(() => {
    if (mermaidRef.current) {
      const svg = mermaidRef.current.querySelector("svg");
      if (svg) {
        svg.style.transform = `scale(${scale})`;
        svg.style.transformOrigin = "top left";
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

  const toggleFilters = () => {
    setOpenFilters((prevState) => !prevState);
  };

  const onSearchBySeqNumber = (e: any) => {
    setSequenceNr(e.target.value);
  };

  const isFilterMatch = (index: number) => {
    if (!sequenceNr) return true;

    const filterSeqNrInt = parseInt(sequenceNr, 10);
    return index + 1 === filterSeqNrInt;
  };

  if (loadingEventMessages)
    return <LoadingOverlay title="Loading Diagram" subtitle="Please wait..." />;

  return (
    <>
      <div className="flex flex-col items-end">
        {hasData ? (
          <>
            <div className="flex justify-end">
              <Tooltip placement="top" title="Filter Messages">
                <IconButton color="primary" onClick={toggleFilters}>
                  <FilterAltIcon />
                </IconButton>
              </Tooltip>
              <Tooltip placement="top" title="Refresh Diagram">
                <IconButton color="primary" onClick={onRefresh}>
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
            <div className="w-full p-2.5">
              <div className="mermaid" ref={mermaidRef}></div>
            </div>
          </>
        ) : (
          <div className="flex w-full justify-center">
            <NoDataOverlay label="No Activity yet" />
          </div>
        )}
      </div>

      {openFilters && (
        <>
          <Dialog
            open={openFilters}
            keepMounted
            fullWidth
            maxWidth="lg"
            onClose={toggleFilters}
          >
            <DialogTitle>All Event Messages</DialogTitle>
            <DialogContent>
              <DialogContentText>
                <div className="flex items-center gap-2.5">
                  <label>Search by Sequence # </label>
                  <TextField
                    onChange={onSearchBySeqNumber}
                    size="small"
                    variant="outlined"
                  />
                </div>
                <List className="w-full" component="nav">
                  {allEventMessages
                    .filter((_: any, index: number) => {
                      return isFilterMatch(index);
                    })
                    .map((message: any, index: number) => {
                      const {
                        msg_type_name: msgType,
                        des_name,
                        src_name,
                        group,
                        group_id,
                        timestamp,
                        src_did,
                        des_did,
                        // msg, TODO: Need to use the content inside the msg to display in the diagram
                      } = message;

                      const formattedTimeStamp = formatDateTime(timestamp);
                      const { groupIcon: IconComponent, groupName } =
                        getGroupById(group);

                      return (
                        <div
                          key={index}
                          style={{ marginBottom: 12 }}
                          className="flex items-center gap-5"
                        >
                          <Chip label={sequenceNr ? sequenceNr : ++index} />
                          <Card style={{ padding: 10 }} className="w-full">
                            <div
                              style={{ marginBottom: 12 }}
                              className="flex justify-between"
                            >
                              <div>
                                <span
                                  style={{
                                    marginBottom: 12,
                                    fontWeight: "bold",
                                  }}
                                  className="flex items-center gap-2"
                                >
                                  {IconComponent} {groupName}{" "}
                                  <Chip label={msgType} />
                                </span>
                                <span>
                                  Sender: {src_name} <Chip label={src_did} /> |{" "}
                                </span>
                                <span>
                                  Receiver: {des_name} <Chip label={des_did} />{" "}
                                  |{" "}
                                </span>
                                <span>Group: {group} | </span>
                                <span>Group ID: {group_id}</span>
                              </div>
                              <span>{formattedTimeStamp}</span>
                            </div>
                            <span className="font-bold">
                              Event Message {sequenceNr ? sequenceNr : index++}
                            </span>
                            <div
                              className="mt-4 flex"
                              style={{
                                border: "1px solid #f1f1f1",
                                borderRadius: 5,
                              }}
                            >
                              <pre className="flex-1 p-2">
                                {JSON.stringify(message, null, 2)}
                              </pre>
                              <div className="shrink-0 p-2">
                                <CopyToClipboard textToCopy={message} />
                              </div>
                            </div>
                          </Card>
                        </div>
                      );
                    })}
                </List>
              </DialogContentText>
            </DialogContent>
            <DialogActions className="p-4">
              <Button variant="contained" onClick={toggleFilters}>
                Close
              </Button>
            </DialogActions>
          </Dialog>
        </>
      )}
    </>
  );
};

export default SequenceDiagram;
