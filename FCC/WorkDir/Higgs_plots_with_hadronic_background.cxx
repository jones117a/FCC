#include "TH1F.h"
#include "TTree.h"
#include "TCanvas.h"
#include "TFile.h"
#include "THStack.h"

void Higgs_plots_with_hadronic_background()
{
    double L = 5000.; //Integrated luminosity in inverse fb
    double xsec_HZ_BR_Hgamgam = 0.7479; //Cross-section * BR in fb
    double N_exp_signal = L * xsec_HZ_BR_Hgamgam;
    double N_gen_signal = 39361;
    double signal_hist_scale_factor = N_exp_signal / N_gen_signal;
    double xsec_Zgam_BR_Zhad = 18589;
    double N_exp_hadronic_background = L * xsec_Zgam_BR_Zhad;
    double N_gen_hadronic_background = 200000;
    double hadronic_background_hist_scale_factor = N_exp_hadronic_background / N_gen_hadronic_background;

    TFile * Signal_File = new TFile("OutDir_1/ee_ZH_Z_Hgamgam_3/heppy.analyzers.examples.zh_hgamgam.TreeProducer.TreeProducer_1/tree.root", "Read");
    TFile * Hadronic_Background_File = new TFile("/afs/cern.ch/work/e/eljones/public/FCCSamples/OutDir_hadronic_background_200k/ee_Zgam_hadronic_200k/heppy.analyzers.examples.zgam_hadronic.TreeProducer.TreeProducer_1/tree.root", "Read");

    TTree * Signal_Tree = (TTree*)Signal_File->Get("events");
    TTree * Hadronic_Background_Tree = (TTree*)Hadronic_Background_File->Get("events");

    TH1F * signal_higgs_mass_hist = new TH1F("signal_higgs_mass", "Mass of reconstructed Higgs particles", 15, 110, 140);
 //   TH1F * signal_higgs_eta_hist = new TH1F("signal_higgs_eta", "Pseudorapidity of reconstructed Higgs particles", 6, -6, 6);
 //   TH1F * signal_higgs_phi_hist = new TH1F("signal_higgs_phi", "Angle of reconstructed Higgs particles from beam axis", 4, -4, 4);
 //   TH1F * signal_lead_photon_pt_hist = new TH1F("signal_lead_photon_pt_hist", "Pt of leading photon in event", 50, 20, 120);
 //   TH1F * signal_sub_lead_photon_pt_hist = new TH1F("signal_sub_lead_photon_pt_hist", "Pt of sub-leading photon in event", 40, 0, 80);
    TH1F * hadronic_background_higgs_mass_hist = new TH1F("hadronic_background_higgs_mass", "Mass of reconstructed Higgs particles", 15, 110, 140);
 //   TH1F * hadronic_background_higgs_eta_hist = new TH1F("hadronic_background_higgs_eta", "Pseudorapidity of reconstructed Higgs particles", 6, -6, 6);
 //   TH1F * hadronic_background_higgs_phi_hist = new TH1F("hadronic_background_higgs_phi", "Angle of reconstructed Higgs particles from beam axis", 4, -4, 4);
 //   TH1F * hadronic_background_lead_photon_pt_hist = new TH1F("hadronic_background_lead_photon_pt_hist", "Pt of leading photon in event", 50, 20, 120);
 //   TH1F * hadronic_background_sub_lead_photon_pt_hist = new TH1F("hadronic_background_sub_lead_photon_pt_hist", "Pt of sub-leading photon in event", 40, 0, 80);

    Signal_Tree->SetBranchStatus("*", 0);
    Signal_Tree->SetBranchStatus("higgs_m", 1);
 //   Signal_Tree->SetBranchStatus("higgs_eta", 1);
 //   Signal_Tree->SetBranchStatus("higgs_phi", 1);
 //   Signal_Tree->SetBranchStatus("lead_photon_pt", 1);
 //   Signal_Tree->SetBranchStatus("sub_lead_photon_pt", 1);
    Hadronic_Background_Tree->SetBranchStatus("*", 0);
    Hadronic_Background_Tree->SetBranchStatus("higgs_m", 1);
 //   Hadronic_Background_Tree->SetBranchStatus("higgs_eta", 1);
 //   Hadronic_Background_Tree->SetBranchStatus("higgs_phi", 1);
 //   Hadronic_Background_Tree->SetBranchStatus("lead_photon_pt", 1);
 //   Hadronic_Background_Tree->SetBranchStatus("sub_lead_photon_pt", 1);

    double signal_higgs_mass;
 //   double signal_higgs_eta;
 //   double signal_higgs_phi;
 //   double signal_lead_photon_pt;
 //   double signal_sub_lead_photon_pt;
    double hadronic_background_higgs_mass;
 //   double hadronic_background_higgs_eta;
 //   double hadronic_background_higgs_phi;
 //   double hadronic_background_lead_photon_pt;
 //   double hadronic_background_sub_lead_photon_pt;

    Signal_Tree->SetBranchAddress("higgs_m", &signal_higgs_mass);
 //   Signal_Tree->SetBranchAddress("higgs_eta", &signal_higgs_eta);
 //   Signal_Tree->SetBranchAddress("higgs_phi", &signal_higgs_phi);
 //   Signal_Tree->SetBranchAddress("lead_photon_pt", &signal_lead_photon_pt);
 //   Signal_Tree->SetBranchAddress("sub_lead_photon_pt", &signal_sub_lead_photon_pt);
    Hadronic_Background_Tree->SetBranchAddress("higgs_m", &hadronic_background_higgs_mass);
 //   Hadronic_Background_Tree->SetBranchAddress("higgs_eta", &hadronic_background_higgs_eta);
 //   Hadronic_Background_Tree->SetBranchAddress("higgs_phi", &hadronic_background_higgs_phi);
 //   Hadronic_Background_Tree->SetBranchAddress("lead_photon_pt", &hadronic_background_lead_photon_pt);
 //   Hadronic_Background_Tree->SetBranchAddress("sub_lead_photon_pt", &hadronic_background_sub_lead_photon_pt);


    for (int higgs_number = 0; higgs_number < Signal_Tree->GetEntries(); ++ higgs_number)
    {
        Signal_Tree->GetEntry(higgs_number);
        signal_higgs_mass_hist->Fill(signal_higgs_mass);
     //   signal_higgs_eta_hist->Fill(signal_higgs_eta);
     //   signal_higgs_phi_hist->Fill(signal_higgs_phi);
     //   signal_lead_photon_pt_hist->Fill(signal_lead_photon_pt);
     //   signal_sub_lead_photon_pt_hist->Fill(signal_sub_lead_photon_pt);
    }
    for (int higgs_number = 0; higgs_number < Hadronic_Background_Tree->GetEntries(); ++ higgs_number)
    {
        Hadronic_Background_Tree->GetEntry(higgs_number);
        hadronic_background_higgs_mass_hist->Fill(hadronic_background_higgs_mass);
     //   hadronic_background_higgs_eta_hist->Fill(hadronic_background_higgs_eta);
     //   hadronic_background_higgs_phi_hist->Fill(hadronic_background_higgs_phi);
     //   hadronic_background_lead_photon_pt_hist->Fill(hadronic_background_lead_photon_pt);
     //   hadronic_background_sub_lead_photon_pt_hist->Fill(hadronic_background_sub_lead_photon_pt);
    }

    signal_higgs_mass_hist->Scale(signal_hist_scale_factor);
    hadronic_background_higgs_mass_hist->Scale(hadronic_background_hist_scale_factor);

    TCanvas * c1 = new TCanvas("c1", "Higgs reconstruction histograms", 800, 600);
    gStyle->SetOptStat(0);
    gStyle->SetOptFit();
 //   c1->Divide(3,2,0,0);

 //   c1->cd(1);
 //   gPad->SetBottomMargin(1);
 //   gPad->SetRightMargin(1);
    signal_higgs_mass_hist->Fit("gaus");
    signal_higgs_mass_hist->SetLineColor(kBlue);
    signal_higgs_mass_hist->SetAxisRange(0., 5000.,"Y");
    hadronic_background_higgs_mass_hist->SetAxisRange(0., 5000., "Y");
    signal_higgs_mass_hist->Draw();
    hadronic_background_higgs_mass_hist->Draw("same");

 //   c1->cd(2);
 //   gPad->SetBottomMargin(1);
 //   gPad->SetRightMargin(1);
 //   gPad->SetLeftMargin(1);
 //   signal_higgs_eta_hist->Draw();
 //   hadronic_background_higgs_eta_hist->Draw();

 //   c1->cd(3);
 //   gPad->SetLeftMargin(1);
 //   gPad->SetRightMargin(1);
 //   gPad->SetBottomMargin(1);
 //   signal_higgs_phi_hist->Draw();
 //   hadronic_background_higgs_phi_hist->Draw();

 //   c1->cd(4);
 //   gPad->SetTopMargin(1);
 //   gPad->SetRightMargin(1);
 //   signal_lead_photon_pt_hist->Draw();
 //   hadronic_background_lead_photon_pt_hist->Draw();

 //   c1->cd(5);
 //   gPad->SetTopMargin(1);
 //   gPad->SetLeftMargin(1);
 //   gPad->SetRightMargin(1);
 //   signal_sub_lead_photon_pt_hist->Draw();
 //   hadronic_background_sub_lead_photon_pt_hist->Draw();

    c1->Update();
    c1->Draw();
    c1->Print("signal_plus_background_200k_histogram.pdf");
    return;
}
