ALTER TABLE `t_appear_red` ADD `diff_times` INT NULL DEFAULT NULL AFTER `not_appear`, ADD `diff_not_appear` INT NULL DEFAULT NULL AFTER `diff_times`;
ALTER TABLE `t_appear_blue` ADD `diff_times` INT NULL DEFAULT NULL AFTER `not_appear`, ADD `diff_not_appear` INT NULL DEFAULT NULL AFTER `diff_times`;
ALTER TABLE `t_appear_red` ADD `score` INT NULL DEFAULT NULL ;
ALTER TABLE `t_appear_blue` ADD `score` INT NULL DEFAULT NULL ;