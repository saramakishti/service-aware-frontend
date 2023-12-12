"use client";

import { useAppState } from "@/components/hooks/useAppContext";
import { NoDataOverlay } from "@/components/noDataOverlay";
import SummaryDetails from "@/components/summary_card";
import CustomTable from "@/components/table";
import { HomeTableConfig } from "@/config/home";
import { useEffect } from "react";
import { mutate } from "swr";

export default function Home() {
  const { data } = useAppState();

  const entitiesKeyFunc = data.entitiesKeyFunc;

  const onRefresh = () => {
    const entityKey =
      typeof entitiesKeyFunc === "function"
        ? entitiesKeyFunc()
        : entitiesKeyFunc;
    if (entitiesKeyFunc) mutate(entityKey);
  };

  useEffect(() => {
    const interval = setInterval(() => {
      onRefresh();
    }, 500);

    return () => clearInterval(interval);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <div className="m-10">
      <SummaryDetails
        entity={{ name: "Home", details: [] }}
        hasRefreshButton={true}
        onRefresh={onRefresh}
        hasAttachDetach={false}
      />

      <div>
        <h4>Home View Table</h4>
        <CustomTable
          loading={data.loadingEntities}
          data={data?.allEntities}
          configuration={HomeTableConfig}
        />
      </div>

      <div>
        <h4>Sequence Diagram</h4>
        <NoDataOverlay label="No Activity yet" />
      </div>
    </div>
  );
}
