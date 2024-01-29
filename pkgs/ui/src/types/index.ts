export interface CustomTableConfiguration {
  key: string;
  label: string;
  render?: (param: any, rowData?: any, onConsume?: any) => void;
}

export interface ICustomTable {
  configuration: CustomTableConfiguration[];
  data: any;
  loading?: boolean;
  tkey: string;
  onConsumeAction?: (param: any) => void;
}

export interface EntityDetails {
  label: string;
  value: string | undefined;
}

export interface Entity {
  name?: string;
  details: EntityDetails[];
}

export interface ISummaryDetails {
  entity: Entity;
  fake?: boolean;
  hasRefreshButton?: boolean;
  onRefresh?: () => void;
}

export interface IEntityActions {
  name: string;
  endpoint: string;
}
