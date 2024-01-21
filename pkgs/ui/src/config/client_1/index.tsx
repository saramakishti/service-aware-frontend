import { Button, Tooltip } from "@mui/material";

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
    render: (value: any) => {
      const onConsume = () => {
        // fetch(value).then(() => { }).catch(() => { })
      };
      return (
        <Button onClick={onConsume} disabled variant="outlined">
          Consume
        </Button>
      );
    },
  },
  {
    key: "entity_did",
    label: "Entity DID",
  },
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
    key: "usage",
    label: "Usage",
    render: (value: any) => {
      let renderedValue = "";

      if (value.length > 0) {
        renderedValue = value.map((item: any, index: number) => {
          return (
            <div key={index}>
              {item.consumer_entity_did} ({item.times_consumed})
            </div>
          );
        });
      }
      return renderedValue;
    },
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
    label: "Actions",
    render: (value: any) => {
      const { data } = value;

      const onButtonClick = (endpoint: string) => {
        console.log("which endpoint comes here?", endpoint);
        // fetch(endpoint).then(() => { }).catch(() => { })
      };

      if (!data) return <div>N/A</div>;

      if (data && data.length)
        return data.map((item: any, index: number) => {
          const buttonLabel = item.name;
          const buttonEndpoint = item.endpoint;

          return (
            <Tooltip placement="top" title={buttonLabel}>
              <Button
                style={{ marginRight: 8 }}
                key={index}
                onClick={() => onButtonClick(buttonEndpoint)}
                size="small"
                variant="outlined"
              >
                {buttonLabel}
              </Button>
            </Tooltip>
          );
        });
    },
  },
];
