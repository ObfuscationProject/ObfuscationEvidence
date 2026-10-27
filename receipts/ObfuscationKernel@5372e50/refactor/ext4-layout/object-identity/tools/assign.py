# Proposed module assignment, bottom to top.
MODULES = {
 "journal": ["jbd2.hpp", "jbd2_replay.hpp", "ext4_recovery.hpp"],
 "layout": ["ext4.hpp", "ext4_times.hpp", "ext4_fs.hpp", "ext4_blocks.hpp", "ext4_readonly.hpp"],
 "extent": ["ext4_first_data_plan.hpp", "ext4_next_data_plan.hpp", "ext4_zero_truncate_plan.hpp",
            "ext4_allocated_empty_data_plan.hpp", "ext4_zero_truncate_witness.hpp",
            "ext4_allocated_empty_data_ownership.hpp", "ext4_allocated_empty_data_witness.hpp",
            "ext4_zero_truncate_preview.hpp", "ext4_allocated_empty_data_journal_verify.hpp",
            "ext4_zero_truncate_journal.hpp", "ext4_allocated_empty_data_journal.hpp",
            "ext4_allocated_empty_data_preview.hpp", "ext4_zero_truncate_transaction_budget.hpp",
            "ext4_allocated_empty_data_transaction_budget.hpp"],
 "alloc": ["ext4_inode_lifetime.hpp", "ext4_free_inode.hpp",
           "ext4_create_plan.hpp", "ext4_create_witness.hpp", "ext4_directory_create_plan.hpp",
           "ext4_directory_create_witness.hpp", "ext4_orphan_chain.hpp", "ext4_orphan_access.hpp",
           "ext4_orphan_ownership.hpp", "ext4_orphan_directory_refs.hpp", "ext4_orphan_reclaim_plan.hpp",
           "ext4_orphan_directory_qualified_reclaim.hpp", "ext4_orphan_reclaim_witness.hpp",
           "ext4_orphan_reclaim_journal.hpp", "ext4_orphan_reclaim_cold.hpp", "ext4_reclaim_history.hpp"],
 "dir": ["ext4_directory_initialization_budget.hpp", "ext4_namespace_plan.hpp", "ext4_rename_plan.hpp",
         "ext4_regular_move_plan.hpp", "ext4_regular_move_witness.hpp", "ext4_namespace_journal.hpp",
         "ext4_namespace_witness.hpp", "ext4_regular_move_journal.hpp"],
 "txn": ["ext4_replay_view.hpp", "ext4_completion.hpp", "metadata_buffers.hpp", "ext4_metadata_transaction.hpp",
         "ext4_create_transaction.hpp", "ext4_first_data_transaction.hpp", "ext4_next_data_transaction.hpp",
         "ext4_rename_transaction.hpp", "ext4_namespace_transaction.hpp", "ext4_regular_move_transaction.hpp",
         "ext4_zero_truncate_session_preview.hpp", "ext4_allocated_empty_data_session_preview.hpp",
         "ext4_zero_truncate_transaction.hpp", "ext4_allocated_empty_data_transaction.hpp"],
 "recovery": ["ext4_replay_shape.hpp", "ext4_namespace_replay.hpp", "ext4_namespace_cold_replay.hpp",
              "ext4_regular_move_replay.hpp", "ext4_regular_move_recovery.hpp", "ext4_regular_move_completion.hpp",
              "ext4_namespace_recovery_binding.hpp", "ext4_namespace_completion.hpp", "ext4_namespace_result_history.hpp",
              "ext4_orphan_reclaim_capture.hpp", "ext4_reclaim_recovery_binding.hpp", "ext4_reclaim_result_history.hpp",
              "ext4_reclaim_composed_budget.hpp", "ext4_reclaim_route_budget.hpp", "ext4_orphan_chain_capture.hpp",
              "ext4_reclaim_composed_history.hpp", "ext4_orphan_snapshot.hpp"],
 "mount": ["ext4_mounted_common_opening_budget.hpp", "ext4_mounted_typed_budget.hpp", "ext4_direct_read_scope.hpp",
           "ext4_mounted_typed_cursor.hpp", "ext4_mounted_startup_workspace.hpp", "ext4_owned_transaction.hpp",
           "ext4_empty_orphan_recovery.hpp", "ext4_mounted_metadata.hpp"],
}
ORDER = list(MODULES)

# SDK contract marker headers stay standalone for the strict SDK validators.
KEEP = ["ext4_directory_create_sdk_profile.hpp", "ext4_mounted_common_profile.hpp"]
