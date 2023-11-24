"use client";

import { NoDataOverlay } from "@/components/noDataOverlay";
import SummaryDetails from "@/components/summary_card";
import CustomTable from "@/components/table";
import {HomeDummyData, HomeTableConfig} from "@/mock/home";

export default function Home() {
  return (
    <div className="m-10">
      <SummaryDetails
        entity={{ name: "Home", details: [] }}
        hasRefreshButton={false}
        hasAttachDetach={false}
      />

      <div>
        <h4>Home View Table</h4>
        <CustomTable data={HomeDummyData} configuration={HomeTableConfig} />
      </div>

      <div>
        <h4>Sequence Diagram</h4>
        <NoDataOverlay label="No Activity yet" />
      </div>
    </div>
  );
}
