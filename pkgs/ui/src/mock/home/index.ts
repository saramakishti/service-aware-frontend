// HOME - Table Data

export const HomeDummyData = [
  {
    entity_name: "C1",
    entity_DID: "did:sov:test:1234",
    network: "Carlo's Home Network",
    ip_address: "127.0.0.1",
    roles: "service repository, service consumer, DLG",
    visible: true,
  },
  {
    entity_name: "C2",
    entity_DID: "did:sov:test:4567",
    network: "Steve's Home Network",
    ip_address: "127.0.0.1",
    roles: "service repository, service consumer, DLG",
    visible: false,
  },
];

export const HomeTableConfig = [
  {
    key: "entity_name",
    label: "Entity name",
  },
  {
    key: "entity_DID",
    label: "Entity DID",
  },
  {
    key: "network",
    label: "Network",
  },
  {
    key: "ip_address",
    label: "IP address",
  },
  {
    key: "roles",
    label: "Roles",
  },
  {
    key: "visible",
    label: "Visible",
  },
];
