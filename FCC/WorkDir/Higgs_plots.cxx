#include "TH1F.h"
#include "TTree.h"
#include "TCanvas.h"
#include "TFile.h"

void Higgs_plots()
{
    TFile * Tree_File = new TFile("OutDir_background/ee_Zgam_hadronic_2/heppy.analyzers.examples.zgam_hadronic.TreeProducer.TreeProducer_1/tree.root", "Read");
    TTree * Tree = (TTree*)Tree_File->Get("events");

    TH1F * higgs_mass_hist = new TH1F("higgs_mass", "Mass of reconstructed Higgs particles", 100, 110, 140);
    TH1F * higgs_eta_hist = new TH1F("higgs_eta", "Pseudorapidity of reconstructed Higgs particles", 100, -6, 6);
    TH1F * higgs_phi_hist = new TH1F("higgs_phi", "Angle of reconstructed Higgs particles from beam axis", 100, -4, 4);
    TH1F * lead_photon_pt_hist = new TH1F("lead_photon_pt_hist", "Pt of leading photon in event", 100, 20, 120);
    TH1F * sub_lead_photon_pt_hist = new TH1F("sub_lead_photon_pt_hist", "Pt of sub-leading photon in event", 100, 0, 80);

    Tree->SetBranchStatus("*", 0);
    Tree->SetBranchStatus("higgs_m", 1);
    Tree->SetBranchStatus("higgs_eta", 1);
    Tree->SetBranchStatus("higgs_phi", 1);
    Tree->SetBranchStatus("lead_photon_pt", 1);
    Tree->SetBranchStatus("sub_lead_photon_pt", 1);

    double higgs_mass;
    double higgs_eta;
    double higgs_phi;
    double lead_photon_pt;
    double sub_lead_photon_pt;

    Tree->SetBranchAddress("higgs_m", &higgs_mass);
    Tree->SetBranchAddress("higgs_eta", &higgs_eta);
    Tree->SetBranchAddress("higgs_phi", &higgs_phi);
    Tree->SetBranchAddress("lead_photon_pt", &lead_photon_pt);
    Tree->SetBranchAddress("sub_lead_photon_pt", &sub_lead_photon_pt);

    for (int higgs_number = 0; higgs_number < Tree->GetEntries(); ++ higgs_number)
    {
        Tree->GetEntry(higgs_number);
        higgs_mass_hist->Fill(higgs_mass);
        higgs_eta_hist->Fill(higgs_eta);
        higgs_phi_hist->Fill(higgs_phi);
        lead_photon_pt_hist->Fill(lead_photon_pt);
        sub_lead_photon_pt_hist->Fill(sub_lead_photon_pt);
    }

    TCanvas * c1 = new TCanvas("c1", "Higgs and leading photon histograms", 800, 600);
    gStyle->SetOptStat(0);
    gStyle->SetOptFit();
    c1->Divide(3,2,0,0);

    c1->cd(1);
    gPad->SetBottomMargin(1);
    gPad->SetRightMargin(1);
    higgs_mass_hist->Draw();
    higgs_mass_hist->Fit("gaus");

    c1->cd(2);
    gPad->SetBottomMargin(1);
    gPad->SetRightMargin(1);
    gPad->SetLeftMargin(1);
    higgs_eta_hist->Draw();

    c1->cd(3);
    gPad->SetLeftMargin(1);
    gPad->SetRightMargin(1);
    gPad->SetBottomMargin(1);
    higgs_phi_hist->Draw();

    c1->cd(4);
    gPad->SetTopMargin(1);
    gPad->SetRightMargin(1);
    lead_photon_pt_hist->Draw();

    c1->cd(5);
    gPad->SetTopMargin(1);
    gPad->SetLeftMargin(1);
    gPad->SetRightMargin(1);
    sub_lead_photon_pt_hist->Draw();

    c1->Update();
    c1->Draw();
    c1->Print("ee_Zgam_hadronic_run_01_Histograms.pdf");
    return;
}
