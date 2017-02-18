Import-Module ActiveDirectory
Import-Csv "C:\Users\Administrator\Desktop\AD_script (1)\users.csv" | ForEach-Object { <#change the file path#>

 $displayName = $_."First name" + " " + $_."Last name"

 $_."First Name" = $_."First Name".ToLower()
 $_."Last name"  = $_."Last name".ToLower()

 $login = ""
 If ($_."Last name".length -ge 7) # 9
 {
    $login = $_."First Name"[0] + $_."Last name".Substring(0,7) # (0, 9)
 }
 Else
 {
    $login = $_."First Name"[0] + $_."Last name"
    $zeros = 8 - $login.length - 1 <# 10 - $login.length - 1#>

    If ($zeros -gt 0)
    {
        $login = $login + "0" * $zeros

    }
    $login = $login + "1"
 }
 $userPrincipalName = $login + "@THEGARDEN.COM" #change the quotes

New-ADUser -Name $_."First name" `
 -Path "OU=this-test,DC=THEGARDEN,DC=COM" <# change the OU, DC, and DC#> `
 -SamAccountName $login `
 -UserPrincipalName $userPrincipalName `
 -Title $_."Position" `
 -OfficePhone $_."Extension" `
 -Division $_."Division" `
 -DisplayName $displayName `
 -AccountPassword (ConvertTo-SecureString "p@ssw0rd1234" -AsPlainText -Force) <#change the password #> `
 -ChangePasswordAtLogon $true `
 -Enabled $true


Write-Output $userPrincipalName $displayName

}
