#!/usr/bin/env python3
"""
Microsoft Fabric & Power BI Pipeline Starter Script
"""

import os
import sys

def main():
    print("=" * 60)
    print("Microsoft Fabric & Power BI Python Pipeline Environment")
    print("=" * 60)

    # 1. Test Azure Identity
    try:
        from azure.identity import DefaultAzureCredential
        print("[+] Azure Identity: Available")
    except ImportError as e:
        print(f"[-] Azure Identity missing: {e}")

    # 2. Test OneLake / ADLS Gen2 SDK
    try:
        from azure.storage.filedatalake import DataLakeServiceClient
        print("[+] Azure Storage DataLake (OneLake SDK): Available")
    except ImportError as e:
        print(f"[-] OneLake SDK missing: {e}")

    # 3. Test Semantic Link (SemPy)
    try:
        import sempy
        import sempy.fabric as fabric
        print(f"[+] SemPy (Fabric Semantic Link): v{sempy.__version__} Available")
    except ImportError as e:
        print(f"[-] SemPy missing: {e}")

    # 4. Test SemPy Labs
    try:
        import sempy_labs
        print("[+] SemPy Labs: Available")
    except ImportError as e:
        print(f"[-] SemPy Labs missing: {e}")

    print("\nNext Steps:")
    print("1. Log in to your Fabric tenant via the Fabric CLI:")
    print("     fab auth login")
    print("2. Check workspaces:")
    print("     fab ls")
    print("3. Or set AZURE_CLIENT_ID, AZURE_CLIENT_SECRET, AZURE_TENANT_ID for automated service principal pipelines.")

if __name__ == "__main__":
    main()
