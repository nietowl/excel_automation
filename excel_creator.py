#!usr/bin/python3
import pandas as pd

# Create a list of sheet names
sheet_names = ["AdiraAric","AidenArden","AinsleyArin","AlaricAris","AlistairAsa","AmariAugustin","AriAva","ArinAvery","ArloBaz","AsherBennett","AugustBranwen","AveryBriar","BazCalla","BennettCassia","BranwenCaspian","BriarCeline","CalanthaCerys","CallaChance","CassiaClementine","CaspianConrad","CelineCora","CerysDax","ChanceDominic","ClementineDora","ConradDorian","CoraEden","DaxEliza","DominicElliot","DoraEmersyn","DorianEvan","EdenFinn","ElizaGenevieve","ElliotGraham","EmersynGray","EvanHazel","FinnIra","GenevieveIris","GrahamJasper","GrayJude","HazelKailani","IraKarter","IrisKellan","JasperKinsley","JudeLeif","KailaniLeo","KarterLila","KellanMaeve","KinsleyMaxen","LeifMiles","LeoMorgan"]

# Create an ExcelWriter object
writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')

for sheet_name in sheet_names:
    # Create a dataframe and write it to the first sheet
    df1 = pd.DataFrame({'first name': [""], 'last name': [""],'userName': [sheet_name], 'Email': [""],'Password': [""], 'Site name': [""], 'Site Url': [""]})
    # Write the dataframe to the current sheet
    df1.to_excel(writer, sheet_name=sheet_name, index=False)

# Save the Excel file
writer.save()