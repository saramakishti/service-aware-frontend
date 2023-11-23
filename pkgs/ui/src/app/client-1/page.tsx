"use client";

import SummaryDetails from "@/components/summary_card";
import { Client1SummaryDetails, Client1DummyData, Client1TableConfig } from "@/mock/client_1";
import CustomTable from "@/components/table";

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
        <div>
            <h4>Consumer View</h4>
            <CustomTable
                data={Client1DummyData}
                configuration={Client1TableConfig}
            />
        </div>
    </div>
  );
}
