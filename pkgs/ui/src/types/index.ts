export interface CustomTableConfiguration {
  key: string;
  label: string;
  render?: (param: any) => void;
}

export interface ICustomTable {
  configuration: CustomTableConfiguration[];
  data: any;
}
