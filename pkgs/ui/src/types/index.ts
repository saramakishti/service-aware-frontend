export interface CustomTableConfiguration {
  key: string;
  label: string;
  render?: (param: any) => void;
}

export interface ICustomTable {
  configuration: CustomTableConfiguration[];
  data: any;
  loading?: boolean;
  tkey: string;
}

export interface EntityDetails {
  label: string;
  value: string;
}

export interface Entity {
  name: string;
  details: EntityDetails[];
}

export interface ISummaryDetails {
  entity: any;
  fake?: boolean;
  hasRefreshButton?: boolean;
  onRefresh?: () => void;
}
