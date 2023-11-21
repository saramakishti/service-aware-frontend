import React from "react";
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

import { NoDataOverlay } from "@/components/noDataOverlay";
import { StyledTableCell, StyledTableRow } from "./style";
import { ICustomTable, CustomTableConfiguration } from "@/types";

const CustomTable = ({ configuration, data }: ICustomTable) => {

  // display empty icon in case there is no data
  if (!data || data.length === 0)
    return <NoDataOverlay label="No Activity yet" />

  const renderTableCell = (value: any, cellKey: string, render?: (param: any) => void | undefined) => {

    let renderedValue = value;

    // cover use case if the data is an array
    if (Array.isArray(value)) renderedValue = value.join(', ')

    // cover use case if we want to render a component
    if (render) renderedValue = render(value);

    return (
      <StyledTableCell key={cellKey} align="left">
        {renderedValue}
      </StyledTableCell>
    );

  }

  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 700 }} aria-label="customized table">
        <TableHead>
          <TableRow>
            {configuration.map((header: CustomTableConfiguration) => (
              <StyledTableCell key={header.key}>
                {header.label}
              </StyledTableCell>
            ))}
          </TableRow>
        </TableHead>
        <TableBody>
          {data.map((data: any, rowIndex: number) => (
            <StyledTableRow key={rowIndex}>
              {configuration.map((column: CustomTableConfiguration) => {
                const cellValue: any = data[column.key];
                const cellKey = column.key;
                const renderComponent = column?.render;
                return renderTableCell(cellValue, cellKey, renderComponent);
              })}
            </StyledTableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  )
}

export default CustomTable;