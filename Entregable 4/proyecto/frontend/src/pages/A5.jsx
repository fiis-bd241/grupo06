import React from "react";
import Sidenav from "../components/Sidenav";
import Navbar from "../components/Navbar";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Stack from "@mui/material/Stack";
import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
//import "../Dash.css";
//import Garea from "../components/garea";
import EmpleadosList from "../components/acabados/operario";
import GareaAca from "../components/acabados/co/garea-acab";
export default function A5() {
  return (
    <>
      <Navbar />
      <Box height={30} />
      <Box sx={{ display: "flex" }}>
        <Sidenav />

        <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
          <h1>Área de Acabados</h1>
          <Typography paragraph>Bienvenido al área estimado Usuario</Typography>

          <Grid container spacing={1} >
            <Grid item xs={8} className="acabadoc">
              <Stack spacing={1}>
                <Card sx={{ maxWidth: 500 }}>
                  <CardContent className="card1">
                    <Stack spacing={1} direction="row">
                      <div className="estadis">
                        <span className="javier-est1">Proceso de acabados</span>
                        <br />
                        <span className="javier-est2">300 Mil</span>
                        <br />
                        <span className="javier-est3">prendas/mes</span>
                      </div>
                    </Stack>
                  </CardContent>
                </Card>
              </Stack>
              <GareaAca />
            </Grid>
            <Grid item xs={4}>
              <Stack spacing={0}>
              <h3>Operarios:</h3>
              <EmpleadosList />
              </Stack>
              </Grid>
          </Grid>
          
        </Box>
      </Box>
    </>
  );
}
