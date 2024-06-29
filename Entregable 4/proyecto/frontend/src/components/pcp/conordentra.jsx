import * as React from 'react';
import PropTypes from 'prop-types';
import Box from '@mui/material/Box';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { styled } from '@mui/system';

function createData(id, name, calories, fat, carbs, protein) {
  return {
    id,
    name,
    calories,
    fat,
    carbs,
    protein,
  };
}

const rows = [
  createData(1, 'Cupcake', 305, 3.7, 67, 4.3, 4),
];

const headCells = [
  { id: 'name', numeric: false, disablePadding: true, label: 'Fecha inicio' },
  { id: 'calories', numeric: true, disablePadding: false, label: 'Fecha fin' },
  { id: 'fat', numeric: true, disablePadding: false, label: 'Prioridad' },
  { id: 'carbs', numeric: true, disablePadding: false, label: 'Estado' },
  { id: 'protein', numeric: true, disablePadding: false, label: 'id_orden_pedido' },
  { id: 'protein', numeric: true, disablePadding: false, label: 'id_plan' },
];

function EnhancedTableHead() {
  return (
    <TableHead>
      <TableRow>
        {headCells.map((headCell) => (
          <TableCell
            key={headCell.id}
            align={headCell.numeric ? 'right' : 'left'}
            padding={headCell.disablePadding ? 'none' : 'normal'}
            style={{ position: 'sticky', top: 0, backgroundColor: 'white', zIndex: 1 }}
          >
            {headCell.label}
          </TableCell>
        ))}
      </TableRow>
    </TableHead>
  );
}

EnhancedTableHead.propTypes = {
  numSelected: PropTypes.number,
  onSelectAllClick: PropTypes.func,
  rowCount: PropTypes.number,
};

export default function EnhancedTable() {
  const StyledTableCell = styled(TableCell)(({ theme }) => ({
    padding: '8px',
    whiteSpace: 'nowrap',
  }));

  return (
    <Box sx={{ width: 500, height: 300 }}>
      <Paper sx={{ width: '100%', height: '100%', overflow: 'auto' }}>
        <TableContainer sx={{ maxHeight: 300 }}>
          <Table stickyHeader size="small">
            <EnhancedTableHead />
            <TableBody>
              {rows.map((row, index) => (
                <TableRow
                  hover
                  role="checkbox"
                  tabIndex={-1}
                  key={row.id}
                  sx={{ cursor: 'pointer' }}
                >
                  <StyledTableCell
                    component="th"
                    scope="row"
                    padding="none"
                  >
                    {row.name}
                  </StyledTableCell>
                  <StyledTableCell align="right">{row.calories}</StyledTableCell>
                  <StyledTableCell align="right">{row.fat}</StyledTableCell>
                  <StyledTableCell align="right">{row.carbs}</StyledTableCell>
                  <StyledTableCell align="right">{row.protein}</StyledTableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Paper>
    </Box>
  );
}
