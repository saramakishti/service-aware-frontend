"use client";

import SummaryDetails from "@/components/summary_card";
import {
    Client2ConsumerData,
    Client2ConsumerTableConfig,
    Client2SummaryDetails
} from "@/mock/client_2";
import CustomTable from "@/components/table";

export default function Client1() {
  return (
    <div className="m-10">
      <SummaryDetails
        hasAttachDetach
        hasRefreshButton
        entity={{
          name: "Client 2",
          details: Client2SummaryDetails,
        }}
      />
        <div>
            <h4>Consumer View</h4>
            <CustomTable
                data={Client2ConsumerData}
                configuration={Client2ConsumerTableConfig}
            />
        </div>
    </div>
  );
}
