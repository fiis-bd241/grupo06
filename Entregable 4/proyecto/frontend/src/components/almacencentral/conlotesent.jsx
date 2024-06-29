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
    fontSize: 10,
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

export default function ConsultaLotesEntrada() {



  return (
    <TableContainer component={Paper}>
      <Table sx={{ maxWidth: 450 }} size="small" aria-label="a dense table">
        <TableHead>
          <StyledTableRow>
          <StyledTableCell>id_lote</StyledTableCell>
            <StyledTableCell>id_materia_prima</StyledTableCell>
          </StyledTableRow>
        </TableHead>
        <TableBody>

            <StyledTableRow >
              <StyledTableCell>--</StyledTableCell>
              <StyledTableCell>--</StyledTableCell>


            </StyledTableRow>

        </TableBody>
      </Table>
    </TableContainer>
  );
}
