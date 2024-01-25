import { Button, IconButton, Tooltip } from "@mui/material";
import AddCircleIcon from "@mui/icons-material/AddCircle";
import RemoveCircleIcon from "@mui/icons-material/RemoveCircle";
import DeleteIcon from "@mui/icons-material/Delete";
import EntityActions from "@/components/entity_actions";

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
    render: (value: any, rowData?: any) => {
      if (value && value?.data.length > 0)
        return <EntityActions rowData={rowData} endpointData={value.data} />;
      else return "N/A";
    },
  },
];
