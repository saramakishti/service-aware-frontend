export const HomeTableConfig = [
  {
    key: "name",
    label: "Entity name",
  },
  {
    key: "did",
    label: "Entity DID",
  },
  {
    key: "network",
    label: "Network",
    render: (value: any) => {
      const renderedValue = typeof value === "object" ? value?.network : "-";
      return renderedValue;
    },
  },
  {
    key: "ip",
    label: "IP address",
  },
  {
    key: "roles",
    label: "Roles",
    render: (value: any) => {
      const renderedValue =
        typeof value === "object" ? value?.roles?.join(", ") : "-";
      return renderedValue;
    },
  },
  {
    key: "attached",
    label: "Attached",
  },
];
