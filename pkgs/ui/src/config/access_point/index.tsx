// AP - Summary

export const APSummaryDetails = [
  {
    label: "DID",
    value: "did:sov:test:1274",
  },
  {
    label: "IP",
    value: "127.0.0.2",
  },
  {
    label: "Network",
    value: "Carlo's Home Network",
  },
];

export const APAttachmentsTableConfig = [
  {
    key: "name",
    label: "Entity name",
  },
  {
    key: "did",
    label: "Entity DID",
  },
  {
    key: "other",
    label: "Network",
    render: (value: any) => {
      let renderedValue = "";
      if (typeof value === "object") renderedValue = value?.network;
      return renderedValue;
    },
  },
  {
    key: "ip",
    label: "IP address",
  },
];

export const APServiceRepositoryTableConfig = [
  {
    key: "service_name",
    label: "Service name",
  },
  {
    key: "service_type",
    label: "Service type",
  },
  {
    key: "endpoint_url",
    label: "End point",
  },
  {
    key: "entity_did",
    label: "Entity DID",
  },
  {
    key: "status",
    label: "Status",
    render: (value: any) => {
      let renderedValue: any = "";
      if (Array.isArray(value.data)) {
        renderedValue = value.data.join(", ");
      } else {
        console.error("Status is not an array", value);
      }
      return renderedValue;
    },
  },
  // {
  //   key: "other",
  //   label: "Type",
  //   render: (value: any) => {
  //     let renderedValue: any = "";
  //     if (typeof value === "object") {
  //       const label = Object.keys(value)[0];
  //       const info = value[label];
  //       renderedValue = (
  //         <code>
  //           {label} {info}
  //         </code>
  //       );
  //     }
  //     return renderedValue;
  //   },
  // },
];
