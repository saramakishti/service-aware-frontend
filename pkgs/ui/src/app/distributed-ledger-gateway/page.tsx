"use client";

import {
  DLGResolutionDummyData,
  DLGResolutionTableConfig,
  DLGSummaryDetails,
} from "@/mock/dlg";
import CustomTable from "@/components/table";
import SummaryDetails from "@/components/summary_card";

export default function DLG() {
  return (
    <div className="m-10">
      <SummaryDetails
        hasRefreshButton
        entity={{
          name: "Distributed Ledger Gateway",
          details: DLGSummaryDetails,
        }}
      />
      <div>
        <h4>DID Resolution View</h4>
        <CustomTable
          data={DLGResolutionDummyData}
          configuration={DLGResolutionTableConfig}
        />
      </div>
    </div>
  );
}
