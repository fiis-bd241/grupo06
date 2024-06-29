import React, { useEffect, useState } from "react";
import Box from "@mui/material/Box";
import { Grid, MenuItem, Select, FormControl, InputLabel } from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import Sidenav from "../../components/Sidenav";
import Navbar from "../../components/Navbar";
import Navigation from "../../components/Navigation";
import DataTable from "../../components/acabados/datatable";
import CajaSalidaTable from "../../components/acabados/co/cajasalidal";
import ImageTooltip from "../../components/acabados/co/image";
// Importar las imágenes
import imagen1 from '../../image/cajasalida.png';
import imagen2 from '../../image/image2.png';
import imagen3 from '../../image/datos_list_a.png';
export default function AcabadoPage() {
  const [empleados, setEmpleados] = useState([]);
  const [selectedEmpleado, setSelectedEmpleado] = useState("");
  const [datos, setDatos] = useState([]);

  useEffect(() => {
    fetch("https://sistema-web-v.onrender.com/sistema/empleadosa/")
      .then((response) => response.json())
      .then((data) => setEmpleados(data));
  }, []);

  useEffect(() => {
    if (selectedEmpleado) {
      fetch(
        `https://sistema-web-v.onrender.com/sistema/datosa/?empleado=${selectedEmpleado}`
      )
        .then((response) => response.json())
        .then((data) => {
          const dataWithIds = data.map((row, index) => ({
            ...row,
            id: row.ID_Caja || index,
          }));
          setDatos(dataWithIds);
        });
    }
  }, [selectedEmpleado]);

  const handleEmpleadoChange = (event) => {
    setSelectedEmpleado(event.target.value);
  };

  const columns = [
    { field: "ID_Caja", headerName: "ID Caja", maxWidth: 80 },
    { field: "nombre", headerName: "Empleado", maxWidth: 80 },
    { field: "cantidad", headerName: "Cantidad", maxWidth: 80 },
    { field: "ID_guia", headerName: "ID Guía", maxWidth: 80 },
    { field: "tipo_prenda", headerName: "Tipo Prenda", maxWidth: 80 },
    { field: "estilo_prenda", headerName: "Estilo Prenda", maxWidth: 80 },
    { field: "talla", headerName: "Talla", maxWidth: 70 },
    { field: "genero", headerName: "Género", maxWidth: 60 },
    { field: "ml", headerName: "ml", maxWidth: 40 },
    { field: "mh", headerName: "mh", maxWidth: 40 },
    { field: "mp", headerName: "mp", maxWidth: 40 },
    { field: "mm", headerName: "mm", maxWidth: 40 },
    { field: "mc", headerName: "mc", maxWidth: 40 },
    { field: "mca", headerName: "mca", maxWidth: 40 },
    { field: "mmu", headerName: "mmu", maxWidth: 40 },
  ];

  return (
    <>
      <Navbar />
      <Box height={30} />
      <Box sx={{ display: "flex" }}>
        <Sidenav />
        <Box component="main" sx={{ flexGrow: 1, p: 1 }}>
          <h1>Área de Acabados</h1>
          <Navigation />
          <Grid container spacing={3} alignItems="center" sx={{ padding: 1 }}>
            <Grid item xs={3}>
              <FormControl fullWidth>
                <InputLabel>Operario</InputLabel>
                <Select
                  value={selectedEmpleado}
                  onChange={handleEmpleadoChange}
                >
                  {empleados.map((empleado) => (
                    <MenuItem key={empleado.nombre} value={empleado.nombre}>
                      {empleado.nombre}
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </Grid>
          </Grid>
          <p>Ver detalle de cajas por Operario en el sistema.</p>
          <ImageTooltip imageUrl={imagen3} />
          <Box mt={3} width={1000}>
            <div style={{ height: 400, width: "100%" }}>
              <DataGrid rows={datos} columns={columns} pageSize={5} />
            </div>
          </Box>
          <h3>Registro de actividad</h3>
          <ImageTooltip imageUrl={imagen2} />
          <DataTable />

          <div className="App">
            <h3>Caja Salida Data</h3>
            <ImageTooltip imageUrl={imagen1} />
            <p>Salida de cajas del área.</p>
            <CajaSalidaTable />
          </div>
        </Box>
      </Box>
    </>
  );
}
