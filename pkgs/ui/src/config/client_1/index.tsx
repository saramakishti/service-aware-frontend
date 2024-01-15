import { Button } from "@mui/material";

export const ClientTableConfig = [
  {
    key: "service_name",
    label: "Service name",
  },
  {
    key: "service_type",
    label: "Service Type",
  },
  {
    key: "endpoint_url",
    label: "End Point",
    render: () => {
      return (
        <Button disabled variant="outlined">
          Consume
        </Button>
      );
    },
  },
  // {
  //   key: "entity",
  //   label: "Entity",
  // },
  {
    key: "entity_did",
    label: "Entity DID",
  },
  // {
  //   key: "network",
  //   label: "Network",
  // },
];

export const ServiceTableConfig = [
  {
    key: "service_name",
    label: "Service name",
  },
  {
    key: "service_type",
    label: "Service Type",
  },
  {
    key: "endpoint_url",
    label: "End Point",
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
  {
    key: "action",
    label: "Action",
    render: (value: any) => {
      let renderedValue: any = "";
      console.log("value", value.data);
      if (typeof value === "object")
        renderedValue = (
          <>
            {value.data.map((actionType: any) => (
              <>
                <Button>{actionType.name}</Button>
              </>
            ))}
          </>
        );
      return renderedValue;
    },
  },
];
