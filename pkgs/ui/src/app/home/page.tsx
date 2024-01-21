"use client";

import { useAppState } from "@/components/hooks/useAppContext";
import SummaryDetails from "@/components/summary_card";
import CustomTable from "@/components/table";
import { HomeTableConfig } from "@/config/home";
import dynamic from "next/dynamic";
import { useEffect } from "react";
import { mutate } from "swr";
import ErrorBoundary from "@/components/error_boundary";

const NoSSRSequenceDiagram = dynamic(
  () => import("../../components/sequence_diagram"),
  { ssr: false },
);

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
    }, 5000);

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
          tkey="home_table"
        />
      </div>

      <div>
        <h4>Sequence Diagram</h4>
        <ErrorBoundary>
          <NoSSRSequenceDiagram />
        </ErrorBoundary>
      </div>
    </div>
  );
}
