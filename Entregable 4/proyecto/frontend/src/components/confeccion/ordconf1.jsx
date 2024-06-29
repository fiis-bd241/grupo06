// consulta de lotes
import React from "react";

// tablas
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell, { tableCellClasses } from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";


//estilos
import { styled } from "@mui/material/styles";

const StyledTableCell = styled(TableCell)(({ theme }) => ({
  [`&.${tableCellClasses.head}`]: {
    backgroundColor: theme.palette.common.black,
    color: theme.palette.common.white,
  },
  [`&.${tableCellClasses.body}`]: {
    fontSize: 9,
  },
}));

const StyledTableRow = styled(TableRow)(({ theme }) => ({
  "&:nth-of-type(odd)": {
    backgroundColor: theme.palette.action.hover,
  },
  // hide last border
  "&:last-child td, &:last-child th": {
    border: 0,
  },
}));

export default function OrdConf1() {



  return (
    <TableContainer component={Paper}>
      <Table sx={{ maxWidth: 450 }} size="small" aria-label="a dense table">
        <TableHead>
          <StyledTableRow>
          <StyledTableCell>id_orden_produccion</StyledTableCell>
            <StyledTableCell>fecha_inicio</StyledTableCell>
            <StyledTableCell>fecha_fin</StyledTableCell>
            <StyledTableCell>estado</StyledTableCell>
            <StyledTableCell>Accion_1</StyledTableCell>
            <StyledTableCell>Accion_2</StyledTableCell>
          </StyledTableRow>
        </TableHead>
        <TableBody>

            <StyledTableRow >
              <StyledTableCell>--</StyledTableCell>
              <StyledTableCell>--</StyledTableCell>
              <StyledTableCell>--</StyledTableCell>
              <StyledTableCell>--</StyledTableCell>
              <StyledTableCell>--</StyledTableCell>
              <StyledTableCell>--</StyledTableCell>

            </StyledTableRow>

        </TableBody>
      </Table>
    </TableContainer>















    
  );
}
