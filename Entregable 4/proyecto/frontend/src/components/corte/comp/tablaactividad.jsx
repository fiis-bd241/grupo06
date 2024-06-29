import React, { useState, useEffect } from 'react';
import axios from 'axios';
import {
  Table, TableBody, TableCell, TableContainer,
  TableHead, TableRow, Paper, Button, Dialog, DialogTitle,
  DialogContent, DialogActions, Typography
} from '@mui/material';

const ActivitiesTable = () => {
  const [activities, setActivities] = useState([]);
  const [selectedActivity, setSelectedActivity] = useState(null);
  const [open, setOpen] = useState(false);

  useEffect(() => {
    axios.get('https://sistema-web-v.onrender.com/sistema/activities/')
      .then(response => {
        setActivities(response.data);
      })
      .catch(error => {
        console.error('Error fetching activities:', error);
      });
  }, []);

  const handleOpen = (id_actividad) => {
    axios.get(`https://sistema-web-v.onrender.com/sistema/activity_details/${id_actividad}/`)
      .then(response => {
        setSelectedActivity(response.data[0]);
        setOpen(true);
      })
      .catch(error => {
        console.error('Error fetching activity details:', error);
      });
  };

  const handleClose = () => {
    setOpen(false);
  };

  return (
    <TableContainer component={Paper}>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>ID Maquina</TableCell>
            <TableCell>Capacidad Total</TableCell>
            <TableCell>Cantidad Actividades</TableCell>
            <TableCell>Fecha Actividad</TableCell>
            <TableCell>Ver Actividad</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {activities.map((activity) => (
            <TableRow key={activity.id_maquina}>
              <TableCell>{activity.id_maquina}</TableCell>
              <TableCell>{activity.capacidad_total}</TableCell>
              <TableCell>{activity.cantidad_actividades}</TableCell>
              <TableCell>{activity.fecha_actividad}</TableCell>
              <TableCell>
                <Button variant="contained" onClick={() => handleOpen(activity.id_actividad)}>
                  Ver Actividad
                </Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>Detalle de Actividad</DialogTitle>
        <DialogContent>
          {selectedActivity && (
            <>
              <Typography>ID Actividad: {selectedActivity.id_actividad}</Typography>
              <Typography>Fecha Actividad: {selectedActivity.fecha_actividad}</Typography>
              <Typography>Cantidad Cortes: {selectedActivity.cantidad_cortes}</Typography>
              <Typography>Cantidad Orden Preproducción: {selectedActivity.cantidad_orden_preproduccion}</Typography>
              <Typography>Progreso Preproducción: {selectedActivity.progreso_preproduccion}%</Typography>
            </>
          )}
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Cerrar</Button>
        </DialogActions>
      </Dialog>
    </TableContainer>
  );
};

export default ActivitiesTable;
