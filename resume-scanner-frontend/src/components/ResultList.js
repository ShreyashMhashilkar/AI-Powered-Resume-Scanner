import React from "react";
import {
  Box,
  Typography,
  Grid,
  Card,
  CardContent,
  Divider,
  Paper,
  Chip,
} from "@mui/material";
import CheckCircleIcon from "@mui/icons-material/CheckCircle";
import DescriptionIcon from "@mui/icons-material/Description";

const CARD_SIZE = { xs: "100%", sm: 700, md: 800 };
const CARD_HEIGHT = { xs: 400, sm: 400, md: 400 };

const ResultList = ({ results }) => (
  <Box mt={4}>
    <Typography
      variant="h4"
      gutterBottom
      sx={{
        fontWeight: "bold",
        mb: 3,
        background: "linear-gradient(90deg, #2a2d9c, #6a0dad)",
        WebkitBackgroundClip: "text",
        WebkitTextFillColor: "transparent",
      }}
    >
      Ranked Candidates
    </Typography>

    <Paper
      elevation={6}
      sx={{
        p: 4,
        borderRadius: 3,
        background: "linear-gradient(145deg, #f9f9ff, #f2f2fa)",
        boxShadow: "0 8px 20px rgba(42, 45, 156, 0.15)",
      }}
    >
      <Grid container spacing={4} alignItems="center" justifyContent="center">
        {results.map((res, idx) => (
          <Grid
            item
            xs={12}
            key={idx}
            sx={{
              display: "flex",
              justifyContent: "center",
            }}
          >
            <Card
              elevation={8}
              sx={{
                width: CARD_SIZE,
                height: CARD_HEIGHT,
                display: "flex",
                flexDirection: "column",
                borderRadius: 4,
                background: "#fff",
                boxShadow:
                  "0 6px 12px rgba(42, 45, 156, 0.12), 0 4px 10px rgba(106, 13, 173, 0.15)",
                transition: "all 0.3s ease",
                "&:hover": {
                  transform: "translateY(-6px)",
                  boxShadow:
                    "0 8px 18px rgba(42, 45, 156, 0.25), 0 6px 16px rgba(106, 13, 173, 0.3)",
                },
              }}
            >
              <CardContent
                sx={{
                  display: "flex",
                  flexDirection: "column",
                  flexGrow: 1,
                  height: "100%",
                  p: 3,
                }}
              >
                {/* Resume file name */}
                <Typography
                  variant="h6"
                  sx={{
                    fontWeight: "bold",
                    mb: 1,
                    display: "flex",
                    alignItems: "center",
                  }}
                >
                  <DescriptionIcon
                    sx={{ mr: 1, verticalAlign: "middle", color: "#6a0dad" }}
                  />
                  {idx + 1}. {res.resume_filename}
                </Typography>

                {/* Score */}
                <Typography
                  variant="body1"
                  sx={{
                    mb: 1,
                    display: "flex",
                    alignItems: "center",
                    gap: 1,
                  }}
                >
                  <CheckCircleIcon color="success" sx={{ fontSize: 20 }} />
                  <strong>Score:</strong> {res.score}
                </Typography>

                <Divider sx={{ mb: 1 }} />

                {/* Resume snippet (original style) */}
                <Box
                  sx={{
                    backgroundColor: "#f5f5f5",
                    padding: 2,
                    borderRadius: 2,
                    whiteSpace: "pre-wrap",
                    fontFamily: "monospace",
                    flexGrow: 1,
                    overflowY: "auto",
                  }}
                >
                  {res.resume_snippet}
                </Box>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Paper>
  </Box>
);

export default ResultList;
