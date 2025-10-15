import React, { useState } from "react";
import { Container, Typography, Paper, CssBaseline } from "@mui/material";
import WorkOutlineIcon from "@mui/icons-material/WorkOutline";
import JobDescriptionForm from "./components/JobDescriptionForm";
import ResumeUpload from "./components/ResumeUpload";
import ResultList from "./components/ResultList";
import LoadingButton from "./components/LoadingButton";
import { ThemeProvider } from "@mui/material/styles";
import theme from "./theme";

function App() {
  const [jd, setJd] = useState("");
  const [resumes, setResumes] = useState([]);
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const onSubmit = async () => {
    if (!jd || resumes.length === 0) {
      alert("Please enter a job description and upload resumes");
      return;
    }

    setLoading(true);
    const formData = new FormData();
    formData.append("jd", jd);
    resumes.forEach((file) => formData.append("resumes", file));

    try {
      const response = await fetch("https://ai-powered-resume-scanner-k9j4.onrender.com/match_rank", {
        method: "POST",
        body: formData,
      });
      const data = await response.json();
      setResults(data.results);
    } catch (error) {
      alert("Error submitting data. Make sure backend is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container maxWidth="md" sx={{ mt: 5, mb: 5 }}>
        <Paper sx={{ p: 4 }}>
          <Typography
            variant="h4"
            gutterBottom
            sx={{ display: "flex", alignItems: "center", gap: 1 }}
          >
            <WorkOutlineIcon sx={{ fontSize: 34 }} color="primary" />
            AI-Powered Resume Scanner
          </Typography>
          <JobDescriptionForm jd={jd} setJd={setJd} />
          <ResumeUpload resumes={resumes} setResumes={setResumes} />
          <LoadingButton onClick={onSubmit} loading={loading} />
        </Paper>
        {results.length > 0 && <ResultList results={results} />}
      </Container>
    </ThemeProvider>
  );
}

export default App;
