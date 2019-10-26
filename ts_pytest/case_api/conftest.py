#!/usr/bin/env python
# coding:utf-8

"""
全局fixtures
"""

import pytest

from common.api.apiOperateExcel import BackupOrNewFile, AnalyzeResults


@pytest.fixture(scope='session', name='bar')
def backup_and_analyze_results():
    """
    全局fixture，备份以及分析测试结果excel
    :return: None
    """
    backup = BackupOrNewFile()
    backup.backup_result_file()
    backup.create_result_file()
    yield
    AnalyzeResults().exec_analysis()