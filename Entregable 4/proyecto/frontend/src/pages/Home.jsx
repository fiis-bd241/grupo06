import React from "react";
import Sidenav from "../components/Sidenav";
import Navbar from "../components/Navbar";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Stack from "@mui/material/Stack";
import "../Dash.css";

import Nos from "../components/nos"; // Ajusta la ruta según tu estructura de archivos

export default function Home() {
  return (
    <>
      <Navbar />
      <Box height={30} />
      <Box sx={{ display: "flex" }}>
        <Sidenav />

        <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
          <h1>Home</h1>
          <Typography paragraph>Bienvenido al sistema Usuario</Typography>

          <Grid container spacing={2}>
            <Grid item xs={8}>
              {/*<Stack spacing={2} direction="row">
                <Card sx={{ maxWidth: 345 }}>
                  <CardContent>
                    <Typography gutterBottom variant="h5" component="div">
                      Lizard
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                      Lizards are a widespread group of squamate reptiles, with
                      over 6,000 species, ranging across all continents except
                      Antarctica
                    </Typography>
                  </CardContent>
                </Card>
                <Card sx={{ maxWidth: 345 }}>
                  <CardContent>
                    <Typography gutterBottom variant="h5" component="div">
                      Lizard
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                      Lizards are a widespread group of squamate reptiles, with
                      over 6,000 species, ranging across all continents except
                      Antarctica
                    </Typography>
                  </CardContent>
                </Card>
              </Stack>*/}

              <div>
                <Nos />
              </div>
            </Grid>
            <Grid item xs={4}>
              <Stack spacing={4}>
                <Card sx={{ maxWidth: 345 }} >
                  <CardContent className="card1">
                    <Stack spacing={2} direction="row">
                      <div className="estadis">
                        <span className="javier-est1">Corte</span><br/>
                        <span className="javier-est2">300 Mil</span><br/>
                        <span className="javier-est3">prendas/mes</span>
                      </div>
                    </Stack>
                  </CardContent>
                </Card>
                <Card sx={{ maxWidth: 345 }}>
                  <CardContent className="card2">
                  <Stack spacing={2} direction="row">
                      <div className="estadis">
                        <span className="javier-est1a">Costura</span><br/>
                        <span className="javier-est2a">300 Mil</span><br/>
                        <span className="javier-est3">prendas/mes</span>
                      </div>
                    </Stack>
                  </CardContent>
                  <Card sx={{ maxWidth: 345 }} >
                  <CardContent className="card3">
                    <Stack spacing={2} direction="row">
                      <div className="estadis">
                        <span className="javier-est1">Proceso de acabado</span><br/>
                        <span className="javier-est2">300 Mil</span><br/>
                        <span className="javier-est3">prendas/mes</span>
                      </div>
                    </Stack>
                  </CardContent>
                </Card>
                <Card sx={{ maxWidth: 345 }}>
                  <CardContent className="card4">
                  <Stack spacing={2} direction="row">
                      <div className="estadis">
                        <span className="javier-est1a">Hangteado</span><br/>
                        <span className="javier-est2a">300 Mil</span><br/>
                        <span className="javier-est3">prendas/mes</span>
                      </div>
                    </Stack>
                  </CardContent>
                </Card>
                </Card>
              </Stack>
            </Grid>
          </Grid>
          <Box height={20} />
          <Grid container spacing={2}>
            <Grid item xs={8}></Grid>
            <Grid item xs={4}></Grid>
          </Grid>
        </Box>
      </Box>
    </>
  );
}
