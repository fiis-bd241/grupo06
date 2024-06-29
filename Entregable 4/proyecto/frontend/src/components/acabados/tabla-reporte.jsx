import React from 'react';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';
import { styled } from '@mui/material/styles';
import { tableCellClasses } from '@mui/material/TableCell';

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
  '&:nth-of-type(odd)': {
    backgroundColor: theme.palette.action.hover,
  },
  '&:last-child td, &:last-child th': {
    border: 0,
  },
}));

export default function TablaReporte({ data }) {
  return (
    <TableContainer component={Paper}>
      <Table sx={{ maxWidth: 900 }} size="small" aria-label="a dense table">
        <TableHead>
          <StyledTableRow>
            <StyledTableCell>ID Empleado</StyledTableCell>
            <StyledTableCell>Nombre</StyledTableCell>
            <StyledTableCell>Primer Apellido</StyledTableCell>
            <StyledTableCell>Segundo Apellido</StyledTableCell>
            <StyledTableCell>ID Correo</StyledTableCell>
            <StyledTableCell>DNI</StyledTableCell>
            <StyledTableCell>ID Cargo</StyledTableCell>
            <StyledTableCell>ID Caja</StyledTableCell>
            <StyledTableCell>Fecha Creación</StyledTableCell>
            <StyledTableCell>Tipo Prenda</StyledTableCell>
          </StyledTableRow>
        </TableHead>
        <TableBody>
          {data.map((row, index) => (
            <StyledTableRow key={index}>
              <StyledTableCell>{row.id_empleado}</StyledTableCell>
              <StyledTableCell>{row.nombre}</StyledTableCell>
              <StyledTableCell>{row.primer_apellido}</StyledTableCell>
              <StyledTableCell>{row.segundo_apellido}</StyledTableCell>
              <StyledTableCell>{row.id_correo}</StyledTableCell>
              <StyledTableCell>{row.dni}</StyledTableCell>
              <StyledTableCell>{row.id_cargo}</StyledTableCell>
              <StyledTableCell>{row.id_caja}</StyledTableCell>
              <StyledTableCell>{row.fecha_creacion}</StyledTableCell>
              <StyledTableCell>{row.tipo_prenda}</StyledTableCell>
            </StyledTableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
