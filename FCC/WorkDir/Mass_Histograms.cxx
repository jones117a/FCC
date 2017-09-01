#include "TH1F.h"
#include "TTree.h"
#include "TCanvas.h"
#include "TFile.h"
#include "THStack.h"

void Mass_Histograms()
{
    double L = 5000.; //Integrated luminosity in inverse fb
    double Xsec_HZ_BR_Hgamgam = 0.4; //Cross-section * BR in fb
    double N_Exp_Signal = L * Xsec_HZ_BR_Hgamgam;
    double N_Gen_Signal = 39361.;
    double Signal_Hist_Scale_Factor = N_Exp_Signal / N_Gen_Signal;
    double Xsec_Zgam = 26460.; //Leading order only
    double N_Exp_Full_Background = L * Xsec_Zgam;
    double N_Gen_Full_Background = 1000000.;
    double Full_Background_Hist_Scale_Factor = N_Exp_Full_Background / N_Gen_Full_Background;

    TFile * Signal_File = new TFile("OutDir_1/ee_ZH_Z_Hgamgam_2/heppy.analyzers.examples.zh_hgamgam.TreeProducer.TreeProducer_1/tree.root", "Read");
    TFile * Full_Background_File = new TFile("/afs/cern.ch/work/e/eljones/public/FCCSamples/OutDir_full_background_1M/ee_Zgam_full_1/heppy.analyzers.examples.zh_hgamgam.TreeProducer.TreeProducer_1/tree.root", "Read");

    TTree * Signal_Tree = (TTree*)Signal_File->Get("events");
    TTree * Full_Background_Tree = (TTree*)Full_Background_File->Get("events");

    THStack * Histogram_Stack = new THStack("Histogram Stack","");

    TH1F * Signal_Higgs_Mass_Hist = new TH1F("Signal_Higgs_Mass", "Mass of reconstructed Higgs particles", 15, 110, 140);
    TH1F * Full_Background_Higgs_Mass_Hist = new TH1F("Full_Background_Higgs_Mass", "Mass of reconstructed Higgs particles", 15, 110, 140);

    Signal_Tree->SetBranchStatus("*", 0);
    Signal_Tree->SetBranchStatus("higgs_m", 1);
    Full_Background_Tree->SetBranchStatus("*", 0);
    Full_Background_Tree->SetBranchStatus("higgs_m", 1);

    double Signal_Higgs_Mass;
    double Full_Background_Higgs_Mass;

    Signal_Tree->SetBranchAddress("higgs_m", &Signal_Higgs_Mass);
    Full_Background_Tree->SetBranchAddress("higgs_m", &Full_Background_Higgs_Mass);

    for (int Higgs_Number = 0; Higgs_Number < Signal_Tree->GetEntries(); ++ Higgs_Number)
    {
        Signal_Tree->GetEntry(Higgs_Number);
        Signal_Higgs_Mass_Hist->Fill(Signal_Higgs_Mass);
    }
    for (int Higgs_Number = 0; Higgs_Number < Full_Background_Tree->GetEntries(); ++ Higgs_Number)
    {
        Full_Background_Tree->GetEntry(Higgs_Number);
        Full_Background_Higgs_Mass_Hist->Fill(Full_Background_Higgs_Mass);
    }

    Signal_Higgs_Mass_Hist->Scale(Signal_Hist_Scale_Factor);
    Full_Background_Higgs_Mass_Hist->Scale(Full_Background_Hist_Scale_Factor);
   
    Full_Background_Higgs_Mass_Hist->Fit("pol1");    

    TCanvas * c1 = new TCanvas("c1", "Higgs reconstruction histograms", 800, 600);
    gStyle->SetOptStat(0);
    gStyle->SetOptFit();
   
    Signal_Higgs_Mass_Hist->SetLineColorAlpha(2, 0.1);
    Signal_Higgs_Mass_Hist->SetLineWidth(3);
    Full_Background_Higgs_Mass_Hist->SetFillStyle(3003);
    Full_Background_Higgs_Mass_Hist->SetFillColorAlpha(4, 0.1);
    Full_Background_Higgs_Mass_Hist->SetLineWidth(3);
    Signal_Higgs_Mass_Hist->SetAxisRange(0., 5000.,"Y");
    Full_Background_Higgs_Mass_Hist->SetAxisRange(0., 5000., "Y");
    Histogram_Stack->Add(Full_Background_Higgs_Mass_Hist);
    Histogram_Stack->Add(Signal_Higgs_Mass_Hist);
    Histogram_Stack->Draw();
    Histogram_Stack->GetXaxis()->SetTitle("Higgs Mass/GeV");
    Histogram_Stack->GetYaxis()->SetTitle("Number of events/2 GeV");
    Histogram_Stack->SetTitle("H -> gamma gamma");
    Histogram_Stack->GetYaxis()->SetTitleOffset(1.4);

    TLegend * Mass_Legend = new TLegend(0.15,0.8,0.25,0.9);
    Mass_Legend->SetHeader("Mass histogram legend");
    Mass_Legend->AddEntry(Signal_Higgs_Mass_Hist, "Signal Histogram", "l");
    Mass_Legend->AddEntry(Full_Background_Higgs_Mass_Hist, "Full Background Histogram", "f");
    Mass_Legend->Draw();

    c1->Update();
    c1->Draw();
    c1->Print("Signal_Plus_Background_Fits.pdf");
    return;
}
