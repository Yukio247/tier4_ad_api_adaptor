// Copyright 2021 TIER IV, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#ifndef OPERATOR_HPP_
#define OPERATOR_HPP_

#include <rclcpp/rclcpp.hpp>
#include <tier4_api_utils/tier4_api_utils.hpp>

#include <autoware_auto_vehicle_msgs/msg/control_mode_report.hpp>
#include <autoware_auto_vehicle_msgs/msg/engage.hpp>
#include <tier4_control_msgs/msg/external_command_selector_mode.hpp>
#include <tier4_control_msgs/msg/gate_mode.hpp>
#include <tier4_control_msgs/srv/external_command_select.hpp>
#include <tier4_external_api_msgs/msg/emergency.hpp>
#include <tier4_external_api_msgs/msg/observer.hpp>
#include <tier4_external_api_msgs/msg/operator.hpp>
#include <tier4_external_api_msgs/srv/set_observer.hpp>
#include <tier4_external_api_msgs/srv/set_operator.hpp>
#include <tier4_system_msgs/msg/operation_mode.hpp>
#include <tier4_system_msgs/srv/operation_mode_request.hpp>

namespace internal_api
{
class Operator : public rclcpp::Node
{
public:
  explicit Operator(const rclcpp::NodeOptions & options);

private:
  using SetOperator = tier4_external_api_msgs::srv::SetOperator;
  using SetObserver = tier4_external_api_msgs::srv::SetObserver;
  using GetOperator = tier4_external_api_msgs::msg::Operator;
  using GetObserver = tier4_external_api_msgs::msg::Observer;
  using ExternalCommandSelect = tier4_control_msgs::srv::ExternalCommandSelect;
  using ExternalCommandSelectorMode = tier4_control_msgs::msg::ExternalCommandSelectorMode;
  using GateMode = tier4_control_msgs::msg::GateMode;
  using OperationMode = tier4_system_msgs::msg::OperationMode;
  using OperationModeRequest = tier4_system_msgs::srv::OperationModeRequest;
  using VehicleEngage = autoware_auto_vehicle_msgs::msg::Engage;
  using VehicleControlMode = autoware_auto_vehicle_msgs::msg::ControlModeReport;

  // ros interface
  rclcpp::CallbackGroup::SharedPtr group_;
  tier4_api_utils::Service<SetOperator>::SharedPtr srv_set_operator_;
  tier4_api_utils::Service<SetObserver>::SharedPtr srv_set_observer_;
  tier4_api_utils::Client<ExternalCommandSelect>::SharedPtr cli_external_select_;
  tier4_api_utils::Client<OperationModeRequest>::SharedPtr cli_operation_mode_;
  rclcpp::Publisher<GateMode>::SharedPtr pub_gate_mode_;
  rclcpp::Publisher<VehicleEngage>::SharedPtr pub_vehicle_engage_;
  rclcpp::Publisher<GetOperator>::SharedPtr pub_operator_;
  rclcpp::Publisher<GetObserver>::SharedPtr pub_observer_;
  rclcpp::Subscription<ExternalCommandSelectorMode>::SharedPtr sub_external_select_;
  rclcpp::Subscription<GateMode>::SharedPtr sub_gate_mode_;
  rclcpp::Subscription<VehicleControlMode>::SharedPtr sub_vehicle_control_mode_;
  rclcpp::Subscription<tier4_external_api_msgs::msg::Emergency>::SharedPtr sub_emergency_;
  rclcpp::TimerBase::SharedPtr timer_;

  // ros callback
  void setOperator(
    const tier4_external_api_msgs::srv::SetOperator::Request::SharedPtr request,
    const tier4_external_api_msgs::srv::SetOperator::Response::SharedPtr response);
  void setObserver(
    const tier4_external_api_msgs::srv::SetObserver::Request::SharedPtr request,
    const tier4_external_api_msgs::srv::SetObserver::Response::SharedPtr response);
  void onExternalSelect(
    const tier4_control_msgs::msg::ExternalCommandSelectorMode::ConstSharedPtr message);
  void onGateMode(const tier4_control_msgs::msg::GateMode::ConstSharedPtr message);
  void onVehicleControlMode(
    const autoware_auto_vehicle_msgs::msg::ControlModeReport::ConstSharedPtr message);
  void onEmergencyStatus(const tier4_external_api_msgs::msg::Emergency::ConstSharedPtr msg);
  void onTimer();

  // class field
  tier4_control_msgs::msg::ExternalCommandSelectorMode::ConstSharedPtr external_select_;
  tier4_control_msgs::msg::GateMode::ConstSharedPtr gate_mode_;
  autoware_auto_vehicle_msgs::msg::ControlModeReport::ConstSharedPtr vehicle_control_mode_;
  tier4_external_api_msgs::msg::Emergency::ConstSharedPtr emergency_status_;
  bool send_engage_in_emergency_;

  // class method
  void publishOperator();
  void publishObserver();
  void setVehicleEngage(bool engage);
  void setGateMode(tier4_control_msgs::msg::GateMode::_data_type data);
  tier4_external_api_msgs::msg::ResponseStatus setVehicleOperationMode(uint8_t mode);
  tier4_external_api_msgs::msg::ResponseStatus setExternalSelect(
    tier4_control_msgs::msg::ExternalCommandSelectorMode::_data_type data);
};

}  // namespace internal_api

#endif  // OPERATOR_HPP_
