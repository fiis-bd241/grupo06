import React, { useState, useEffect } from "react";
import Sidenav from "../../components/Sidenav";
import Navbar from "../../components/Navbar";
import { Button, Box, TextField, Grid } from "@mui/material";
import DraggableDialog from "../../components/acabados/popupimp";
import Navigation from "../../components/Navigation";
import TablaReporte from "../../components/acabados/tabla-reporte";
import Bot from "../../components/acabados/bot";
import SkeletonLoader from "../SkeletonLoader";
import axios from 'axios';
import ImageTooltip from "../../components/acabados/co/image";
import imagen5 from '../../image/reporteacabados.png';
export default function Reporte() {
  const [open, setOpen] = useState(false);
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState([]);
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  useEffect(() => {
    setTimeout(() => {
      setLoading(false);
    }, 1500);
  }, []);

  const handleBuscar = async () => {
    try {
      const response = await axios.get('https://sistema-web-v.onrender.com/sistema/acabadoreporte', {
        params: { fecha_inicio: startDate, fecha_fin: endDate }
      });
      setData(response.data);
    } catch (error) {
      console.error('Error al buscar datos:', error);
    }
  };

  return (
    <>
      <Navbar />
      <Box height={30} />
      <Box sx={{ display: "flex" }}>
        <Sidenav />

        <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
          {loading ? (
            <SkeletonLoader />
          ) : (
            <>
              <h1>Área de Acabados</h1>
              <div>
                <Navigation />
              </div>

              <Grid container spacing={3} alignItems="center" sx={{ padding: 2 }}>
                <Grid item xs={3}>
                  <TextField
                    id="date-start"
                    label="Fecha inicio"
                    type="date"
                    value={startDate}
                    onChange={(e) => setStartDate(e.target.value)}
                    InputLabelProps={{ shrink: true }}
                    fullWidth
                  />
                </Grid>
                <Grid item xs={3}>
                  <TextField
                    id="date-end"
                    label="Fecha fin"
                    type="date"
                    value={endDate}
                    onChange={(e) => setEndDate(e.target.value)}
                    InputLabelProps={{ shrink: true }}
                    fullWidth
                  />
                </Grid>
                <Grid item xs={2}>
                  <Button
                    variant="contained"
                    sx={{ backgroundColor: "#881C62", color: "white" }}
                    onClick={handleBuscar}
                  >
                    Buscar
                  </Button>
                </Grid>
                <Grid item xs={2}>
                  <Button
                    variant="contained"
                    sx={{ backgroundColor: "green", color: "white" }}
                    onClick={handleClickOpen}
                  >
                    Imprimir
                  </Button>
                  <DraggableDialog open={open} handleClose={handleClose} />
                </Grid>
                <Grid item xs={1}>
                  <Bot />
                </Grid>
              </Grid>
              <ImageTooltip imageUrl={imagen5} />
              <Box>
                <TablaReporte data={data} />
              </Box>
            </>
          )}
        </Box>
      </Box>
    </>
  );
}
