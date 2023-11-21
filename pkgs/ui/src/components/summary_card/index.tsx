"use client";
import { useRef } from "react";
import CopyToClipboard from "@/components/copy_to_clipboard";
import {
  Button,
  Card,
  CardContent,
  CardHeader,
  Typography,
} from "@mui/material";
import { EntityDetails, ISummaryDetails } from "@/types";

const SummaryDetails = ({
  entity,
  hasRefreshButton,
  hasAttachDetach,
}: ISummaryDetails) => {
  const cardContentRef = useRef(null);
  const hasDetails = entity.details && entity.details.length > 0;

  return (
    <>
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
        }}
      >
        <h2>{entity.name}</h2>
        <div>
          {hasAttachDetach && (
            <Button className="mr-6" variant="contained">
              Attach / Detach
            </Button>
          )}
          {hasRefreshButton && <Button variant="contained">Refresh</Button>}
        </div>
      </div>
      {hasDetails && (
        <Card variant="outlined">
          <CardHeader
            subheader="Summary"
            action={<CopyToClipboard contentRef={cardContentRef} />}
          />
          <CardContent ref={cardContentRef}>
            {entity.details.map((info: EntityDetails, index: number) => {
              return (
                <Typography key={index} color="text.primary" gutterBottom>
                  {info.label}: <code>{info.value}</code>
                </Typography>
              );
            })}
          </CardContent>
        </Card>
      )}
    </>
  );
};
export default SummaryDetails;
