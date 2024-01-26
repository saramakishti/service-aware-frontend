"use client";

import { mutate } from "swr";
import { useGetAttachedEntities } from "@/api/entities/entities";
import { useGetAllRepositories } from "@/api/repositories/repositories";
import SummaryDetails from "@/components/summary_card";
import CustomTable from "@/components/table";
import {
  APAttachmentsTableConfig,
  APServiceRepositoryTableConfig,
} from "@/config/access_point";
import { useEffect } from "react";
import useGetEntityByNameOrDid from "@/components/hooks/useGetEntityByNameOrDid";
import { projectConfig } from "@/config/config";

export default function AccessPoint() {
  const { entity } = useGetEntityByNameOrDid("AP");
  const {
    data: APAttachementData,
    isLoading: loadingAttachements,
    swrKey: attachedEntitiesKeyFunc,
  } = useGetAttachedEntities();
  const {
    data: APRepositories,
    isLoading: laodingRepositories,
    swrKey: repositoriesKeyFunc,
  } = useGetAllRepositories();

  const onRefresh = () => {
    const attachedEntitiesKey =
      typeof attachedEntitiesKeyFunc === "function"
        ? attachedEntitiesKeyFunc()
        : attachedEntitiesKeyFunc;
    const repositoriesKey =
      typeof repositoriesKeyFunc === "function"
        ? repositoriesKeyFunc()
        : repositoriesKeyFunc;

    if (attachedEntitiesKey) {
      mutate(attachedEntitiesKey);
    }
    if (repositoriesKey) {
      mutate(repositoriesKey);
    }
  };

  useEffect(() => {
    const interval = setInterval(() => {
      onRefresh();
    }, projectConfig.REFRESH_FREQUENCY);

    return () => clearInterval(interval);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <div className="m-10">
      <SummaryDetails
        hasRefreshButton
        onRefresh={onRefresh}
        entity={{
          name: "Access Point",
          details: [
            {
              label: "DID",
              value: entity?.did,
            },
            {
              label: "IP",
              value: entity?.ip,
            },
            {
              label: "Network",
              value: entity?.network,
            },
          ],
        }}
      />
      <div>
        <h4>Attachment View</h4>
        <CustomTable
          loading={loadingAttachements}
          data={APAttachementData?.data}
          configuration={APAttachmentsTableConfig}
          tkey="attachment-table"
        />
      </div>
      <div>
        <h4>Service Repository View </h4>
        <CustomTable
          loading={laodingRepositories}
          data={APRepositories?.data}
          configuration={APServiceRepositoryTableConfig}
          tkey="service-repository-table"
        />
      </div>
    </div>
  );
}
