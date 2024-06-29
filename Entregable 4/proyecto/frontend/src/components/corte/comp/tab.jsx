// DraggableDialog.jsx
import React from 'react';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';
import Paper from '@mui/material/Paper';
import Draggable from 'react-draggable';
// tablas
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell, { tableCellClasses } from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';


//estilos
import { styled } from '@mui/material/styles';


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
    '&:nth-of-type(odd)': {
      backgroundColor: theme.palette.action.hover,
    },
    // hide last border
    '&:last-child td, &:last-child th': {
      border: 0,
    },
  }));


function PaperComponent(props) {
  return (
    <Draggable handle="#draggable-dialog-title" cancel={'[class*="MuiDialogContent-root"]'}>
      <Paper {...props} />
    </Draggable>
  );
}

export default function DraggableDialog({ open, handleClose }) {
  return (
    <Dialog
      open={open}
      onClose={handleClose}
      PaperComponent={PaperComponent}
      aria-labelledby="draggable-dialog-title"
      sx={{ '& .MuiDialog-paper': { width: '800px', maxWidth: 'none' } }}
    >
      <DialogTitle style={{ cursor: 'move' }} id="draggable-dialog-title">
        Cortes que se realizan por actividad
      </DialogTitle>
      <DialogContent>
      <TableContainer component={Paper}>
<Table sx={{ maxWidth: 600}} size="small" aria-label="a dense table">
  <TableHead>
    <StyledTableRow>
    <StyledTableCell>Id_actividad</StyledTableCell>
    <StyledTableCell>fecha_actividad</StyledTableCell>
    <StyledTableCell>cantidad_cortes</StyledTableCell>
    <StyledTableCell>cantidad_orden_produc</StyledTableCell>
    <StyledTableCell>progreso_produc</StyledTableCell>

    </StyledTableRow>
    </TableHead>
    <TableBody>
   
    <StyledTableRow>
    <StyledTableCell >--</StyledTableCell>
    <StyledTableCell >--</StyledTableCell>
    <StyledTableCell >--</StyledTableCell>
    <StyledTableCell >--</StyledTableCell>
    <StyledTableCell >--</StyledTableCell>
    </StyledTableRow>
  
    </TableBody>
  </Table>
</TableContainer>

      </DialogContent>
      <DialogActions>
        <Button autoFocus onClick={handleClose}>
          Regresar
        </Button>
      </DialogActions>
    </Dialog>
  );
}
