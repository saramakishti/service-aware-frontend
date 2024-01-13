import { Button } from "@mui/material";

export const Client2ConsumerTableConfig = [
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

export const Client2ProducerTableConfig = [
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
  },
  {
    key: "other",
    label: "Action",
    render: (value: any) => {
      let renderedValue: any = "";
      if (typeof value === "object")
        renderedValue = (
          <>
            {value.action.map((actionType: string) => (
              <>
                <code>{actionType}</code>
                <br />
              </>
            ))}
          </>
        );
      return renderedValue;
    },
  },
];
