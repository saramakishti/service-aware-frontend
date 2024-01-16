import React from "react";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";

import { NoDataOverlay } from "@/components/noDataOverlay";
import { StyledTableCell, StyledTableRow } from "./style";
import { ICustomTable, CustomTableConfiguration } from "@/types";
import { Checkbox, Skeleton } from "@mui/material";
import ErrorBoundary from "@/components/error_boundary";

const CustomTable = ({ configuration, data, loading, tkey }: ICustomTable) => {
  if (loading)
    return <Skeleton variant="rectangular" animation="wave" height={200} />;

  // display empty icon in case there is no data
  if (!data || data.length === 0)
    return <NoDataOverlay label="No Activity yet" />;

  const renderTableCell = (
    value: any,
    cellKey: string,
    render?: (param: any) => void | undefined,
  ) => {
    let renderedValue = value;

    // cover use case if the data is an array
    if (Array.isArray(value)) renderedValue = value.join(", ");

    // cover use case if the data is an boolean
    if (typeof value === "boolean")
      renderedValue = <Checkbox disabled checked={value} />;

    // cover use case if we want to render a component
    if (render) renderedValue = render(value);
    if (typeof renderedValue === "object" && render === undefined) {
      console.warn("Missing render function for column " + cellKey);
    }
    return (
      <ErrorBoundary>
        <StyledTableCell key={cellKey} align="left">
          {renderedValue}
        </StyledTableCell>
      </ErrorBoundary>
    );
  };

  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 700 }} aria-label="customized table">
        <TableHead>
          <TableRow>
            {configuration.map((header: CustomTableConfiguration) => (
              <StyledTableCell key={header.key}>{header.label}</StyledTableCell>
            ))}
          </TableRow>
        </TableHead>
        <TableBody>
          {data.map((data: any, rowIndex: number) => (
            <StyledTableRow key={rowIndex}>
              {configuration.map(
                (column: CustomTableConfiguration, columnIndex: number) => {
                  const cellValue: any = data[column.key];
                  const cellKey = tkey + ":" + column.key + ":" + rowIndex;
                  const renderComponent = column?.render;
                  return renderTableCell(
                    cellValue,
                    cellKey + ":" + columnIndex,
                    renderComponent,
                  );
                },
              )}
            </StyledTableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default CustomTable;
