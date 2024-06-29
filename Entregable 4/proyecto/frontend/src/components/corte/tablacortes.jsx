import React from "react";

// tablas
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell, { tableCellClasses } from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";

import TablePagination from "@mui/material/TablePagination";

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

export default function TablaCortesLotes() {
  const [page, setPage] = React.useState(0);
  const [rowsPerPage, setRowsPerPage] = React.useState(10);

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(+event.target.value);
    setPage(0);
  };
  return (
    <Paper sx={{ width: "90%", overflow: "hidden" }}>
      <TableContainer sx={{ maxHeight: 440 }}>
        <Table stickyHeader aria-label="sticky table">
          <TableHead>
            <StyledTableRow>
              <StyledTableCell>id_orden_produccion</StyledTableCell>
              <StyledTableCell>cantidad</StyledTableCell>
              <StyledTableCell>id_lote</StyledTableCell>
              <StyledTableCell>cantidad_lote</StyledTableCell>
              <StyledTableCell>tipo_corte</StyledTableCell>
              <StyledTableCell>cantidad_cortes</StyledTableCell>
              <StyledTableCell>estado_orden</StyledTableCell>
              <StyledTableCell>progreso_prodyccion</StyledTableCell>

            </StyledTableRow>
          </TableHead>
          <TableBody>
            <StyledTableRow>
              <StyledTableCell>-</StyledTableCell>
              <StyledTableCell>-</StyledTableCell>
              <StyledTableCell>-</StyledTableCell>
              <StyledTableCell>-</StyledTableCell>
              <StyledTableCell>-</StyledTableCell>
              <StyledTableCell>-</StyledTableCell>
              <StyledTableCell>-</StyledTableCell>
              <StyledTableCell>-</StyledTableCell>
             </StyledTableRow>
          </TableBody>
        </Table>
      </TableContainer>
      <TablePagination
        rowsPerPageOptions={[10, 25, 100]}
        component="div"
        rowsPerPage={rowsPerPage}
        page={page}
        onPageChange={handleChangePage}
        onRowsPerPageChange={handleChangeRowsPerPage}
      />
    </Paper>
  );
}
