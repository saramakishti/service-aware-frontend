"use client";

import SummaryDetails from "@/components/summary_card";
import { Client1SummaryDetails } from "@/mock/client_1";

export default function Client1() {
  return (
    <div className="m-10">
      <SummaryDetails
        hasAttachDetach
        hasRefreshButton
        entity={{
          name: "Client 1",
          details: Client1SummaryDetails,
        }}
      />
    </div>
  );
}
